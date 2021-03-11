from django.contrib import admin


class FilmAdmin(admin.ModelAdmin):
    fields = ('creation_year',)
    readonly_fields = ('creation_year',)

    @staticmethod
    def creation_year(obj):
        return obj.year
