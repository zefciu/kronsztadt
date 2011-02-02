# vim: set fileencoding=utf-8
<%inherit file="/base.mako" />

<%def name="head()">
</%def>

${h.random_img()}

<%def name="lang_switch(current)" >
<%
	txt, new  = ('Polski', 'pol') if current == 'rus' else ('Русский', 'rus')
%>
	${h.link_to(txt, h.url_for(
			controller = 'entries', action = 'display', slug = c.entry.slug,
			lang = new
	))}
</%def>

<div>
${c.entry.get_trans(c.lang).content}
</div>
<div>
${lang_switch(c.lang)}
</div>
<div>
	${h.link_to('Losuj', h.url_for(
			controller = 'entries', action = 'random'
			))}
</div>
