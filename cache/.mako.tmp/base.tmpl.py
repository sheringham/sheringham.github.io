# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520780734.169
_enable_loop = True
_template_filename = u'themes/lanyon/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'header', context._clean_inheritance_tokens(), templateuri=u'base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'header')] = ns

    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    ns = runtime.TemplateNamespace(u'annotations', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'annotations')] = ns

    ns = runtime.TemplateNamespace(u'footer', context._clean_inheritance_tokens(), templateuri=u'base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        header = _mako_get_namespace(context, 'header')
        base = _mako_get_namespace(context, 'base')
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        lanyon_subtheme = _import_ns.get('lanyon_subtheme', context.get('lanyon_subtheme', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        __M_writer(u'\r\n')
        __M_writer(u'\r\n')
        __M_writer(u'\r\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\r\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\r\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\r\n</head>\r\n')
        if lanyon_subtheme:
            __M_writer(u'<body class="')
            __M_writer(unicode(lanyon_subtheme))
            __M_writer(u'">\r\n')
        else:
            __M_writer(u'<body>\r\n')
        __M_writer(u'    <a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(unicode(messages("Skip to main content")))
        __M_writer(u'</a>\r\n    <!-- Target for toggling the sidebar `.sidebar-checkbox` is for regular\r\n            styles, `#sidebar-checkbox` for behavior. -->\r\n    <input type="checkbox" class="sidebar-checkbox" id="sidebar-checkbox">\r\n\r\n    <!-- Toggleable sidebar -->\r\n    <div class="sidebar" id="sidebar">\r\n        <div class="sidebar-item">\r\n            <p>A reserved <a href="https://getnikola.com" target="_blank">Nikola</a> theme that places the utmost gravity on content with a hidden drawer. Made by <a href="https://twitter.com/mdo" target="_blank">@mdo</a> for Jekyll,\r\n            ported to Nikola by <a href="https://twitter.com/ralsina" target="_blank">@ralsina</a>.</p>\r\n        </div>\r\n        ')
        __M_writer(unicode(header.html_navigation_links()))
        __M_writer(u'\r\n    </div>\r\n\r\n    <!-- Wrap is the content to shift when toggling the sidebar. We wrap the\r\n         content to avoid any CSS collisions with our real content. -->\r\n    <div class="wrap">\r\n      <div class="masthead">\r\n        <div class="container">\r\n          ')
        __M_writer(unicode(header.html_site_title()))
        __M_writer(u'\r\n        </div>\r\n      </div>\r\n\r\n      <div class="container content" id="content">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\r\n        ')
        __M_writer(unicode(footer.html_footer()))
        __M_writer(u'\r\n      </div>\r\n    </div>\r\n    <label for="sidebar-checkbox" class="sidebar-toggle"></label>\r\n    ')
        __M_writer(unicode(body_end))
        __M_writer(u'\r\n    ')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\r\n    ')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\r\n    <!-- fancy dates -->\r\n    <script>\r\n    moment.locale("')
        __M_writer(unicode(momentjs_locales[lang]))
        __M_writer(u'");\r\n    fancydates(')
        __M_writer(unicode(date_fanciness))
        __M_writer(u', ')
        __M_writer(unicode(js_date_format))
        __M_writer(u');\r\n    </script>\r\n    <!-- end fancy dates -->\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"134": 8, "144": 8, "150": 56, "23": 3, "26": 2, "29": 5, "32": 4, "35": 0, "165": 150, "62": 2, "63": 3, "64": 4, "65": 5, "66": 6, "67": 6, "68": 7, "69": 7, "74": 10, "75": 11, "76": 11, "77": 13, "78": 14, "79": 14, "80": 14, "81": 15, "82": 16, "83": 18, "84": 18, "85": 18, "86": 29, "87": 29, "88": 37, "89": 37, "94": 42, "95": 43, "96": 43, "97": 47, "98": 47, "99": 48, "100": 48, "101": 49, "102": 49, "103": 52, "104": 52, "105": 53, "106": 53, "107": 53, "108": 53, "113": 56, "119": 42}, "uri": "base.tmpl", "filename": "themes/lanyon/templates/base.tmpl"}
__M_END_METADATA
"""
