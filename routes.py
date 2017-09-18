from flask import jsonify
from flask import render_template
from flask import flash
from flask import current_app
from flask import make_response
from flask import abort
from flask import request

#from decorators import authenticate

import process 

TOKEN_HEADER_NAME = "MY_AUTH_TOKEN"
def init_api_routes(app):
    if app:
        app.add_url_rule('photos/<string:id>', 'photos_by_id', photos_by_id,, methods=['GET']) 
        '''app.add_url_rule('/api/candidates/<string:id>', 'candidate_by_id', candidate_by_id, methods=['GET'])
        app.add_url_rule('/api/candidates', 'candidate', candidate, methods=['GET'])
        app.add_url_rule('/api/candidates', 'add_candidate', add_candidate, methods=['POST'])
        app.add_url_rule('/api/candidates/<string:id>', 'update_candidate', update_candidate, methods=['PUT'])
        app.add_url_rule('/api/candidates/random', 'get_one_random_candidate', random_candidates,
                         methods=['GET'], defaults={'nr_of_items': 1})
        app.add_url_rule('/api/candidates/random/<int:nr_of_items>', 'get_random_candidates', random_candidates,
                         methods=['GET'])
        app.add_url_rule('/api/candidates/<string:id>', 'delete_candidate', delete_candidate, methods=['DELETE'])
        app.add_url_rule('/api/projects/random/<int:nr_of_items>', 'get_random_projects', random_projects,
                         methods=['GET'])
        app.add_url_rule('/api/projects', 'add_project', add_project, methods=['POST'])
        app.add_url_rule('/api/initdb', 'initdb', initialize_database)
        app.add_url_rule('/api/filldb', 'filldb', fill_database)
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        '''
#@authenticate(is_user_valid_func=is_user_valid)
def page_about(*args, **kwargs):
    #if current_app:
    #    flash('The application was loaded', 'info')
    #    flash('The secret key is {0}'.format(current_app.config['SECRET_KEY']), 'info')

    resp = make_response(render_template('about.html', selected_menu_item="about"))
    #resp.headers[TOKEN_HEADER_NAME] = kwargs[TOKEN_HEADER_NAME]
    return resp



def page_photos():
    #my_cookie = request.cookies.get('myCookie')
    #print('COOKIE FROM THE CLIENT:' + my_cookie)
    #current_candidates = candidate(serialize=False)
    missions = [{'id': '1', 'name': 'Powell Street Parking'}, {'id': '2', 'name': 'Emeryville Carpool'}, {'id': '3','name': '2200 Parking'}]
    return render_template('photos.html', selected_menu_item="photos", missions=missions)

def photos_by_id(id):
    rv = process.process_all_new_executions(id)
    if rv:
        #maybe only the new ones? should always be the latest one...
        processed_executions = filter_by_id(get_all_mission_executions(process.PROCESSED_PATH, False), id)
        mission_ids = ['1', '2', '3']
        mission_id_to_label = {'1': 'Powell Street Parking', '2': 'Emeryville Carpool', '3': '2200 Parking'}
        #TAKE OUT JSON DUMPS 
        executions_serialized = [execution.serialize() for execution in processed_executions]
        
        #dictionary mapping from ymd to an array of all images on that day, sorted by reverse timestamp
        executions_by_ymd = {} 
        for execution_serialized in executions_serialized:
            ymd = execution_serialized["ymd"]
            if ymd not in executions_by_ymd:
                executions_by_ymd[ymd] = []
            executions_by_date.append(execution_serialized)
            
        #make sure these are sorted in reverse time order for each day 
        for ymd in executions_by_ymd:
            executions_by_ymd[ymd].sort(key = lambda x: x["hms"], reverse = true)
            
        return render_template('photos.html', selected_menu_item="photos", executions_by_ymd=executions_by_ymd, id=id, mission_id_to_label=mission_id_to_label, mission_ids=mission_ids)
    else:
        return "NO_NEW_DATA"


def page_index():
    resp = make_response(render_template('index.html', selected_menu_item="index"))
    resp.set_cookie('myCookie','this is a custom cookie sent from the server')
    return resp


def crash_server():
    abort(500)

'''
def initialize_database():
    message_key = "Initialize Database"
    try:
        init_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))

    return jsonify(build_message(message_key, "OK"))


def fill_database():
    message_key = "Fill Database"
    try:
        fill_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))

    return jsonify(build_message(message_key, "OK"))
'''

def init_website_routes(app):
    if app:
        app.add_url_rule('/crash', 'crash_server', crash_server, methods=['GET'])
        app.add_url_rule('/about', 'page_about', page_about, methods=['GET'])
        app.add_url_rule('/photos', 'page_photos', page_photos, methods=['GET'])
        app.add_url_rule('/', 'page_index', page_index, methods=['GET'])


def handle_error_404(error):
    flash('Server says: {0}'.format(error), 'error')
    return render_template('404.html', selected_menu_item=None)


def handle_error_500(error):
    flash('Server says: {0}'.format(error), 'error')
    return render_template('500.html', selected_menu_item=None)


def init_error_handlers(app):
    if app:
        app.error_handler_spec[None][404] = handle_error_404
        app.error_handler_spec[None][500] = handle_error_500


def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({'routes': result, 'total': len(result)})
