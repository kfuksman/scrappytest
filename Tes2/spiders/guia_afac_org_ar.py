from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, GuiaAfacItem, GuiaAfac1Item


class GuiaAfacOrgAr(BasePortiaSpider):
    name = "guia.afac.org.ar"
    allowed_domains = ['guia.afac.org.ar']
    start_urls = ['http://guia.afac.org.ar/empresas.php?h=1&tipoe=1&lg=SP']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                GuiaAfacItem,
                None,
                'tr:nth-child(2) > td, tr:nth-child(2) > tbody > td',
                [
                    Field(
                        'texto_completo',
                        'tr:nth-child(2) > td > .txt_info_cliente *::text, tr:nth-child(2) > tbody > td > .txt_info_cliente *::text',
                        []),
                    Field(
                        'mail',
                        'tr:nth-child(2) > td > .txt_info_cliente > span > a::attr(href), tr:nth-child(2) > tbody > td > .txt_info_cliente > span > a::attr(href)',
                        []),
                    Field(
                        'web',
                        'tr:nth-child(2) > td > .txt_info_cliente > a:nth-child(11)::attr(href), tr:nth-child(2) > tbody > td > .txt_info_cliente > a:nth-child(11)::attr(href)',
                        [])])]]
