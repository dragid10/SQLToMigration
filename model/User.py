class User:
    def __init__(self, role_id, is_miami, name, email, password, has_deleted, remember_token, created_at, updated_at):
        self.role_id = role_id
        self.is_miami = is_miami
        self.name = name
        self.email = email
        self.password = password
        self.has_deleted = has_deleted
        self.remember_token = remember_token
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return """
                'role_id' => '{role_id}', 
                'is_miami' => '{is_miami}', 
                'name' => '{name}', 
                'email' => '{email}', 
                'password' => '{password}', 
                'has_deleted' => '{has_deleted}', 
                'remember_token' => '{remember_token}', 
                'created_at' => '{created_at}', 
                'updated_at' => '{updated_at}', 
                        """.format(role_id=self.role_id, is_miami=self.is_miami, name=self.name, email=self.email,
                                   password=self.password, has_deleted=self.has_deleted,
                                   remember_token=self.remember_token, created_at=self.created_at,
                                   updated_at=self.updated_at).rstrip().lstrip()
