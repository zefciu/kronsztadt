<%inherit file="/base.mako" />

<%def name="head()">
</%def>

<h1>Nowy wpis</h1>
${h.form(h.url_for(controller='entries', action='new_entry'), method='post')}
${h.text('slug')} <br />
${h.textarea('content_rus')}<br />
${h.textarea('content_pol')}<br />
${h.submit(None, u'Zapisz')}<br />
${h.end_form()}
