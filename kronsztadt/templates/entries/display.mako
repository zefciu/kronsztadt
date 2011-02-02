# vim: set fileencoding=utf-8
<%inherit file="/base.mako" />

<%def name="head()">
</%def>

<%def name="lang_switch(current)" >
<%
	txt, new  = ('Polski', 'pol') if current == 'rus' else ('Русский', 'rus')
%>
	${h.link_to(txt, h.url_for(
			controller = 'entries', action = 'display', slug = c.entry.slug,
			lang = new
	))}
</%def>

<div id="left-bar">
	<div id="navi">
		<div>
		${lang_switch(c.lang)}
		</div>
		<div>
			${h.link_to('Losuj' if c.lang == 'pol' else 'Случайный', h.url_for(
					controller = 'entries', action = 'random'
					))}
		</div>
		<div class="clear"></div>
	</div>

	<div id="icon">
		${h.random_img()}
	</div>
</div>

<div id="content">
${c.entry.get_trans(c.lang).content}
</div>
