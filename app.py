
class GuideSchema(ma.Schema):
    class Meta:
        fields: ('title', 'content')

guide_schema = GuideSchema()
guides_schemas = GuideSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)
