#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-10 14:59
# @Author  : zhangzhen
# @Site    : 
# @File    : lite.py
# @Software: PyCharm
from typing import Any, Dict, Text

from rasa.nlu.emulators import NoEmulator


class EntityEmulator(NoEmulator):
    def __init__(self) -> None:
        self.name = "entity"

    def normalise_request_json(self, data: Dict[Text, Any]) -> Dict[Text, Any]:
        return data

    def normalise_response_json(self, data: Dict[Text, Any]) -> Dict[Text, Any]:
        """Transform data to target format."""
        if 'intent' in data:
            del data['intent']

        if 'project' in data:
            del data['project']

        if 'model' in data:
            del data['model']

        if 'adapter' in data:
            del data['adapter']

        if 'entities' in data:
            entities = data.get('entities')
            del data['entities']
        else:
            entities = []
        spans = [{'start': ent['start'], 'end': ent['end'], 'label': ent['entity']} for ent in entities]
        data.update({'spans': spans})

        return data
