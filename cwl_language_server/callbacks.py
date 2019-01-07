#!/usr/bin/env python
import pylspclient.lsp_structs as structs
import sys
from linecache import getline


def initialize(params): # InitializeParams -> InitializeResult
    return {
        'capabilities': {
            'completionProvider': {
                'triggerCharacters': [': '],
            },
        },
    }

def initialized(params): # InitializedParams -> None
    return

def completion(params): # CompletionParams -> CompletionList
    # print('Params: ', params, file=sys.stderr)
    params = params['params']
    ctx = params['context']
    line = params['position']['line']
    col = params['position']['character']
    uri = params['textDocument']['uri']

    field = getline(uri, line+1)[0:col].lstrip().rstrip(': ')
    if not field:
        return structs.CompletionList(False, [])

    return completion_list.get(field, structs.CompletionList(False, []))

completion_list = {
    'cwlVersion': [
        structs.CompletionItem('draft-2',      deprecated=True),
        structs.CompletionItem('draft-3.dev1', deprecated=True),
        structs.CompletionItem('draft-3.dev2', deprecated=True),
        structs.CompletionItem('draft-3.dev3', deprecated=True),
        structs.CompletionItem('draft-3.dev4', deprecated=True),
        structs.CompletionItem('draft-3.dev5', deprecated=True),
        structs.CompletionItem('draft-3',      deprecated=True),
        structs.CompletionItem('draft-4.dev1', deprecated=True),
        structs.CompletionItem('draft-4.dev2', deprecated=True),
        structs.CompletionItem('draft-4.dev3', deprecated=True),
        structs.CompletionItem('v1.0.dev4',    deprecated=True),
        structs.CompletionItem('v1.0'),
    ],
}

def to_dict(obj):
    """Return a dictionary object for obj.
    All the fields with None values are omitted.
    It is used for debugging purpose."""
    if obj is None:
        return obj
    if isinstance(obj, list):
        return [to_dict(o) for o in obj if o is not None]
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, object):
        return { k:v for k, v in obj.__dict__.items() if v is not None }
    return obj

if __name__ == '__main__':
    pass
