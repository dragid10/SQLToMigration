class Role:
    name = ''
    created_at = '2019-03-06 22:23:29'
    updated_at = '2019-03-06 22:23:29'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return """
            'name' => '{name}',
            'created_at' => '{created}',   
            'updated_at' => '{update}'   
        """.format(name=self.name, created=self.created_at, update=self.updated_at).rstrip().lstrip()
