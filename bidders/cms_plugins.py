# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from bidders_cms_integration.models import BidderPluginModel

class BidderPluginPublisher(CMSPluginBase):
    model = BidderPluginModel  # model where plugin data are saved
    module = "조달업체 앱"
    name = "조달업체 플러그인"  # name of the plugin in the interface
    render_template = "bidders_cms_integration/bidder_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(BidderPluginPublisher)  # register the plugin
