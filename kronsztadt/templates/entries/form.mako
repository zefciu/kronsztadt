<%inherit file="base.mako" />

<%def name="head()">
</%def>

<h1>Nowy wpis</h1>
${h.form(h.url_for(controller='entries', action='new_entry'), method='post')}
${h.textarea(content_rus)}
${h.textarea(content_pol)}
${h.submit(None, u'Zapisz')}
${h.end_form()}
