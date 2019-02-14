class Migration:
    id = 0
    migration = ""
    batch = 1

    def __init__(self, migration):
        # self.id = id
        self.migration = migration

    def __str__(self):
        return """
            'migration' => '{name}',
            'batch' => '{batch}'   
        """.format(name=self.migration, batch=self.batch).rstrip().lstrip()
