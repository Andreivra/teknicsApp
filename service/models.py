from django.db import models


class Company(models.Model):
    select_status_options = [('garantie', 'Garantie'), ('post_garantie', 'Post Garantie'), ('extern', 'Extern')]

    company_name = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=30)
    agent_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    task_description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    select_status = models.CharField(choices=select_status_options, max_length=13)
#    trainer = models.ForeignKey(Mecanic, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # auto-now_add salveaza data si ora de creere
    updated_at = models.DateTimeField(auto_now=True)  # auto_now salveaza data ora cand se modifica intrarea

    def __str__(self):
        return f"{self.company_name} {self.task_description}"
