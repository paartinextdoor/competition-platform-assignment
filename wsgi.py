import click, pytest, sys
from flask import Flask
from flask.cli import AppGroup
from tabulate import tabulate
from App.database import db, get_migrate
from App.models import Student, Result, Registry
from App.main import create_app
from App.controllers import (create_user, get_all_users, initialize, create_comp, list_comps, 
                             add_participant, list_participants, get_results_file, update_results, update_comp,
                             remove_participant, delete_comp, delete_user)
from datetime import datetime


app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''
user_cli = AppGroup('user', help='User object commands') 

@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("usertype", default="student")
def create_user_command(username, password, usertype):
    create_user(username, password, usertype)
    print(f'{username} created!')

@user_cli.command("list", help="Lists users in the database")
def list_user_command():
    users = get_all_users()
    headers = ["User ID", "Username", "Type"]
    table = []
    for user in users:
        table.append([user.id, user.username, user.usertype])
    print(tabulate(table, headers, tablefmt="fancy_grid"))

@user_cli.command("register", help="Register participants for competition")
@click.argument("studentid", type=int)
@click.argument("compid", type=int)
def register_user_command(studentid, compid):
    add_participant(studentid, compid)

@user_cli.command("unregister", help="unregister participants for competition")
@click.argument("registryid", type=int)
def unregister_user_command(registryid):
    remove_participant(registryid)

@user_cli.command("delete-user", help="delete user")
@click.argument("id", type=int)
def delete_user_command(id):
    delete_user(id)

app.cli.add_command(user_cli)


'''
Comp Commands
'''
comp_cli = AppGroup('comp', help='competition')

@comp_cli.command("create", help="Create competition")
@click.argument("hostid", type=int)
@click.argument("compname", type=str)
@click.argument("description", default="Coding competition", type=str)
@click.argument("dateofcomp", type=str) 
def create_comp_command(hostid, compname, description, dateofcomp):
    try:
        
        comp_date = datetime.strptime(dateofcomp, "%Y-%m-%d").date()
    except ValueError:
        
        raise click.BadParameter("Invalid date format. Please provide date in 'YYYY-MM-DD' format.")
  
    create_comp(hostid, compname, description, comp_date)

@comp_cli.command("update-result", help="Update results")
@click.argument("studentid", type=int)
@click.argument("compid", type=int)
@click.argument("score", type=float)
def update_results_command(studentid, compid, score):
    update_results(studentid, get_results_file(compid).fileID, score)

@comp_cli.command("update-comp", help="Update competition")
@click.argument("compid", type=int)
@click.option("--compname")
@click.option("--description")
@click.option("--dateofcomp")
def update_comp_command(compid, compname, description, dateofcomp):
    if dateofcomp:
        try:
            comp_date = datetime.strptime(dateofcomp, "%Y-%m-%d").date()
        except ValueError:
            raise click.BadParameter("Invalid date format. Please provide date in 'YYYY-MM-DD' format.")
    update_comp(compID=compid, compName=compname, description=description, dateOfComp=dateofcomp)

@comp_cli.command("list", help="list all competitions")
def list_comps_command():
    comps = list_comps()
    headers = ["Comp ID", "Host ID", "Competition Name", "Date", "Description", "Participants"]
    table = []
    for comp in comps:
        num_participants = Registry.query.filter_by(compID=comp.compID).count()
        table.append([comp.compID, comp.hostID, comp.compName, comp.dateOfComp, comp.description, num_participants])
    print(tabulate(table, headers, tablefmt="fancy_grid"))

@comp_cli.command("list-participants", help="list all participants in competition")
@click.argument("compid", type=int)
def list_participants_command(compid):
    participants = list_participants(compid)
    headers = ["Student ID", "Registry ID", "Username", "Score", "Rank"]
    table = []
    for participant in participants:
        student = Student.query.get(participant.studentID)
        if student:
            results = Result.query.filter_by(studentID=student.id, fileID=get_results_file(compID=compid).fileID).first()
            table.append([student.id, participant.id, student.username, results.score, results.rank])
    table.sort(key=lambda x: x[4], reverse=False)
    print(tabulate(table, headers, tablefmt="fancy_grid"))

@comp_cli.command("delete-comp", help="delete competition")
@click.argument("compid", type=int)
def delete_competition(compid):
    delete_comp(compID=compid)

app.cli.add_command(comp_cli)

