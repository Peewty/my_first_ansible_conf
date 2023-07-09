#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import MySQLdb

#Definition of Ansible module argument
#We define two argument db_name for connection of the databse and request for execute a query in base
def main():
    module = AnsibleModule(
        argument_spec=dict(
        db_name = dict(required=True, type='str'),
        request = dict(required=True, type='str'),
        )
    )

    #Retrieving argument values of module
    db_name_local = module.params.get('db_name')
    request_local = module.params.get('request')

    #connection to database, execute query and storage the result in result variable
    db = MySQLdb.connect(db=db_name_local)
    cur = db.cursor()
    cur.execute(request_local)
    results = cur.fetchall()
    db.close()

    #We use module.exit_json for send result to Ansible
    module.exit_json(change=False, resultat=results)

if __name__ == "__main__":
    main()

DOCUMENTATION='''
module: count_page
author: Quentin
description: Module who execute SQL Query

options:
    db_name:
        description: Name of database
        required: yes
    request:
        description: Query to execute
        required: yes
'''

EXAMPLES='''
- names: "SQL query execution"
  count_pages:
    db_name: "name of your DB"
    request: "select * from user;"
'''

RETURN = '''
resultat:
    description: returns query result
'''