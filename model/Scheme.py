class Scheme:
    key = ''
    name = ''
    order = ''
    type = ''
    created_at = '2019-03-06 22:23:29'
    updated_at = '2019-03-06 22:23:29'
    category = ''

    def __init__(self, key, name, order, type, category):
        self.key = key
        self.name = name
        self.order = order
        self.type = type
        self.category = category

    def __str__(self):
        return """
            'key' => '{key}',
            'name' => '{name}',   
            'order' => '{order}',   
            'type' => '{type}',   
            'created_at' => '{created}',   
            'updated_at' => '{updated}',   
            'category' => '{category}',   
        """.format(key=self.key, name=self.name, order=self.order, type=self.type, created=self.created_at,
                   updated=self.updated_at, category=self.category).rstrip().lstrip()
