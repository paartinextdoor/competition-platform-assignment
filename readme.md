# Competititon Platform
## Documentation
Available Commands:
--------------------
1. User Commands (Prefix: user)
   - create: Creates a user with a username, password, and user type.
   @user_cli.command("create", help="Creates a user")
    $ flask user create <username><password><usertype>

   - list: Lists all users in the database.
    @user_cli.command("list", help="Lists users in the database")
    $ flask user list 

   - register: Registers a participant for a competition by student and competition ID.
    @user_cli.command("register", help="Register participants for competition")
    $ flask user register <studentID><compID>

   - unregister: Unregisters a participant from a competition using the registry ID.
    @user_cli.command("unregister", help="unregister participants for competition")
    $ flask user unregister <registryID>

   - delete-user: Deletes a user by user ID.
   @user_cli.command("delete-user", help="delete user")
   $ flask user delete-user <id>

2. Competition Commands (Prefix: comp)
   - create: Creates a competition with a host ID, name, description, and competition date.
    @comp_cli.command("create", help="Create competition")
    $ flask comp create <hostid> <compname> <description> <dateofcomp>

   - update-result: Updates the score for a student in a specific competition.
    @comp_cli.command("update-result", help="Update results")
    $ flask comp update-result <studentid> <compid> <score>

   - update-comp: Updates the details of a competition.
    @comp_cli.command("update-comp", help="Update competition")
    $ flask comp update-comp <compid> <--compname> <--description> <--dateofcomp>

   - list: Lists all competitions.
    @comp_cli.command("list", help="list all competitions")
    $ flask comp list

   - list-participants: Lists all participants of a competition by competition ID.
    @comp_cli.command("list-participants", help="list all participants in competition")
    $ flask comp list-participants <compID>

   - delete-comp: Deletes a competition by ID.
   @comp_cli.command("delete-comp", help="delete competition")
   $ flask comp delete-comp <compID>
