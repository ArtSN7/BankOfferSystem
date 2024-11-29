from datetime import datetime
from flask import (
    Flask, request, render_template, url_for,
    redirect, flash, session,
)

from utils.auth_of_manager import getting_response_of_auth
from utils.checks import allowed_file, login_required
from utils.common import get_flash_msg_data as msg
from utils.forms import LoginForm
import utils.stubs as stub

from utils.requests_for_front import get_user_data, get_all_leads_data
from utils.add_data_from_uploaded_file import open_file
from utils.create_file_for_manager import main_calling_func

app = Flask(__name__)
app.secret_key = 'b8f6b1e4a0e6c7d8f8e5e'


# проверено - работает
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' in session:
        user_data = get_user_data(session.get('user_id'))
        user_full_name = session.get('user_full_name')
        return render_template('index.html',
                               user_data=user_data,
                               user_full_name=user_full_name)

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = getting_response_of_auth(form.username.data, form.password.data)
        if user:
            session['user_id'] = user['id']
            session['user_full_name'] = user['manager_name']
            return redirect(url_for('index'))

        flash(*msg('wrong_auth'))

    return render_template('login.html',
                           form=form)


@app.route('/clients', methods=['GET', 'POST'])
@login_required
def clients():
    leads_on_queue_count = stub.get_leads_on_queue_count()
    all_leads_data = get_all_leads_data(session.get('user_id')) # получает данные лида
    curr_date = datetime.now().strftime("%d.%m.%Y")

    if request.method == 'POST':
        if 'load_data' in request.form:
            stub.transfer_leads_to_sales_table()
            flash(*msg('leads_transferred'))

        elif 'download' in request.form:
            stub.download_all_leads_data()

            main_calling_func(session.get('user_id'), 'all_leads.xlsx')


            flash(*msg('file_downloaded'))

    user_full_name = session.get('user_full_name')
    return render_template(
        'client_data_page.html',
        all_leads_data=all_leads_data,
        leads_on_queue_count=leads_on_queue_count,
        user_full_name=user_full_name,
        curr_date=curr_date,
    )


@app.route('/client_data_sending', methods=['GET', 'POST'])
@login_required
def send_client_data(): # проверено - работает
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            data = stub.convert_to_dict(file)
            is_valid = stub.validate_client_data(data)

            open_file(file.filename) # transfer all the data to the DB


            if is_valid:
                stub.process_client_data(data)
                flash(*msg('file_sent'))
            else:
                flash(*msg('data_not_valid'))
        else:
            flash(*msg('wrong_file_format'))

    user_full_name = session.get('user_full_name')
    return render_template('client_data_form.html',
                           user_full_name=user_full_name)

# проверено - работает  
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_full_name', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
