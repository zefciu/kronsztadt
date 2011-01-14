<%inherit file="/base.mako" />

<%def name="head()">
</%def>

${c.entry.translations[c.lang].content}

% if lang == 'rus':
% h.link
