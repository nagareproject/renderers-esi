# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""Edge Server-side Include renderer

https://www.w3.org/TR/esi-lang
"""

from nagare.renderers import xml
from nagare.renderers.xml import TagProp


class Renderer(xml.XmlRenderer):
    """ The ESI renderer
    """

    namespace = 'http://www.edge-delivery.org/esi/1.0'

    # The ESI tags
    # ------------

    include = TagProp('include', {'src', 'alt', 'onerror'})
    inline = TagProp('inline', {'name', 'fetchable'})
    choose = TagProp('choose')
    when = TagProp('when', {'test'})
    otherwise = TagProp('otherwise')
    try_ = TagProp('try')
    attempt = TagProp('attempt')
    except_ = TagProp('except')
    comment = TagProp('comment', {'text'})
    remove = TagProp('remove')
    vars = TagProp('vars')

    def __init__(self, parent=None, *args, **kw):
        super(Renderer, self).__init__(parent, *args, **kw)

        self.namespaces = {'esi': self.namespace}
        self.default_namespace = 'esi'

    def esi(self, text):
        """Generate a ``esi`` comment element

        In:
          - ``text`` -- comment text

        Return:
          - the comment element
        """
        return super(Renderer, self).comment('esi ' + text)
