from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Blog(models.Model):
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"
    body = RichTextUploadingField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


