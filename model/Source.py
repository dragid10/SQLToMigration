class Source:
    oid = ''
    reference_type = ''
    content = ''
    source = ''
    source_date = ''
    summary = ''
    comments = ''
    comment_user_id = ''
    source_type = ''
    citation = ''

    def __init__(self, oid, reference_type, content, source, source_date, summary, comments, comment_user_id,
                 source_type, citation):
        self.citation = citation
        self.source_type = source_type
        self.comment_user_id = comment_user_id
        self.comments = comments
        self.summary = summary
        self.source_date = source_date
        self.source = source
        self.content = content
        self.reference_type = reference_type
        self.oid = oid

    def __str__(self):
        return """
            'oid' => '{oid}',
            'reference_type' => '{reference_type}',   
            'content' => '{content}',   
            'source' => '{source}',   
            'summary' => '{summary}',   
            'comments' => '{comments}',   
            'comment_user_id' => '{comment_user_id}',   
            'source_type' => '{source_type}',   
            'citation' => '{citation}',   
        """.format(oid=self.oid, reference_type=self.reference_type, content=self.content, source=self.source,
                   summary=self.summary,
                   comments=self.comments, comment_user_id=self.comment_user_id, source_type=self.source_type,
                   citation=self.citation).rstrip().lstrip()
