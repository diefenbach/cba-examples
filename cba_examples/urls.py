from django.conf.urls import url

from cba_examples.views import checkbox
from cba_examples.views import drag_n_drop
from cba_examples.views import file_input_1
from cba_examples.views import file_input_2
from cba_examples.views import links
from cba_examples.views import list_1
from cba_examples.views import image
from cba_examples.views import overview
from cba_examples.views import radio
from cba_examples.views import select_1
from cba_examples.views import select_2
from cba_examples.views import select_3
from cba_examples.views import textarea_1
from cba_examples.views import textarea_2
from cba_examples.views import text_input_1
from cba_examples.views import text_input_2


urlpatterns = [
    url(r'^$', overview.OverviewView.as_view(), name='overview'),
    url(r'^checkboxes$', checkbox.CheckboxView.as_view(), name='checkboxes'),
    url(r'^drag-n-drop$', drag_n_drop.DragnDropView.as_view(), name='drag_n_drop'),
    url(r'^links$', links.LinksView.as_view(), name='link'),
    url(r'^list-1$', list_1.LinksView.as_view(), name='list_1'),
    url(r'^file-input-1$', file_input_1.FileInputView.as_view(), name='file_input_1'),
    url(r'^file-input-2$', file_input_2.FileInputView.as_view(), name='file_input_2'),
    url(r'^image$', image.ImageView.as_view(), name='image'),
    url(r'^radio$', radio.RadioCheckboxView.as_view(), name='radio'),
    url(r'^select-1$', select_1.SelectView.as_view(), name='select_1'),
    url(r'^select-2$', select_2.SelectView.as_view(), name='select_2'),
    url(r'^select-3$', select_3.SelectView.as_view(), name='select_3'),
    url(r'^textarea-1$', textarea_1.TextAreaView.as_view(), name='textarea_1'),
    url(r'^textarea-2$', textarea_2.TextAreaView.as_view(), name='textarea_2'),
    url(r'^text-input-1$', text_input_1.TextInputView.as_view(), name='text_input_1'),
    url(r'^text-input-2$', text_input_2.TextInputView.as_view(), name='text_input_2'),
]
