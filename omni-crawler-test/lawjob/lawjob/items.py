# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import  TakeFirst, MapCompose
from w3lib.html import remove_tags


class LawjobItem(scrapy.Item):
    # required fields
    title = Field(output_processor=TakeFirst())
    # a unique id for the job on the crawled site.
    job_id = Field()
    # the url the job was crawled from
    url = Field()
    # name of the company where the job is.
    company = Field()

    # location of the job.
    # should ideally include city, state and country.
    # postal code if available.
    # does not need to include street information
    location = Field()
    description = Field()

    # the url users should be sent to for viewing the job. Sometimes
    # the "url" field requires a cookie to be set and this "apply_url" field will be differnt
    # since it requires no cookie or session state.
    apply_url = Field()

    # optional fields
    industry = Field()
    baseSalary = Field()
    benefits = Field()
    requirements = Field()
    skills = Field()
    work_hours = Field()
