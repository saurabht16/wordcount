from crispy_forms.bootstrap import InlineField, FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

class CustomerListFormHelper(FormHelper):
    form_id = 'customer-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    form_method = 'GET'
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Customer Records',
                    InlineField('account_number'),
                    InlineField('customer_last_name'),
                    InlineField('customer_first_name'),
                    InlineField('primary_phone'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
)