# --
# Copyright (c) 2008-2018 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.renderers import xml
from nagare.renderers.esi import Renderer


def test_namespaces():
    e = Renderer()
    assert e.try_(e.include).tostring() == b'<esi:try xmlns:esi="http://www.edge-delivery.org/esi/1.0"><esi:include/></esi:try>'

    e = Renderer()
    e.default_namespace = None
    assert e.try_(e.include).tostring() == b'<try xmlns:esi="http://www.edge-delivery.org/esi/1.0"><include/></try>'

    e = Renderer()
    e.namespaces = None
    e.default_namespace = None
    assert e.try_(e.include).tostring() == b'<try><include/></try>'

    e = Renderer()
    x = xml.Renderer()
    root = x.content(x.section(e.try_(e.include)), x.section(e.try_(e.include)))
    assert root.tostring() == b'<content><section><esi:try xmlns:esi="http://www.edge-delivery.org/esi/1.0"><esi:include/></esi:try></section><section><esi:try xmlns:esi="http://www.edge-delivery.org/esi/1.0"><esi:include/></esi:try></section></content>'


def test_escape():
    e = Renderer()
    x = xml.Renderer()

    root = x.div(e.esi('<p><esi:vars>Hello, $(HTTP_COOKIE{name})!</esi:vars></p>'))
    assert root.tostring() == b'<div><!--esi <p><esi:vars>Hello, $(HTTP_COOKIE{name})!</esi:vars></p>--></div>'
