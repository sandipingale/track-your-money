from django.forms import ModelForm
from shares.models import Share

class ShareForm(ModelForm):
    class Meta:
        model = Share
        fields = ["symbol", "company_name", "tnx_type", "quantity", "txn_price", "txn_date"]