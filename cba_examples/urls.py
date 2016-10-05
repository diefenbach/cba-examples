from django.conf.urls import url

from cba_examples.views import checkbox
from cba_examples.views import overview
from cba_examples.views import radio
from cba_examples.views import text_input_1
from cba_examples.views import text_input_2
from cba_examples.views import select_1
from cba_examples.views import select_2
from cba_examples.views import drag_n_drop


urlpatterns = [
    url(r'^$', overview.OverviewView.as_view(), name='overview'),
    url(r'^drag-n-drop$', drag_n_drop.DragnDropView.as_view(), name='drag_n_drop'),
    url(r'^checkboxes$', checkbox.CheckboxView.as_view(), name='checkboxes'),
    url(r'^radio$', radio.RadioCheckboxView.as_view(), name='radio'),
    url(r'^select-1$', select_1.SelectView.as_view(), name='select_1'),
    url(r'^select-2$', select_2.SelectView.as_view(), name='select_2'),
    url(r'^text-input-1$', text_input_1.TextInputView.as_view(), name='text_input_1'),
    url(r'^text-input-2$', text_input_2.TextInputView.as_view(), name='text_input_2'),
]
