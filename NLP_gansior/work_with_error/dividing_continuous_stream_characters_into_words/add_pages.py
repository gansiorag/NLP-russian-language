"""AI is creating summary for 

Returns:
    [type]: [description]
"""
from tkinter import Frame
from ModulesInterface.page1 import Page1
from ModulesInterface.pred_work_text import page_pred_work
from ModulesInterface.searches_sources import SearchS


def add_page(osn_loc, name_p: str, text: str):
    """AI is creating summary for add_page

    Args:
        osn_loc ([type]): [description]
        text (str): [description]

    Returns:
        [type]: [description]
    """

    page_loc = None
    match name_p:
        case 'page_start':
            ppp = Page1(osn_loc)
            page_loc = ppp.page1
        case 'page_pred_work':
            ppp = page_pred_work(osn_loc)
            page_loc = ppp.page_base
        case 'searches_sources':
            ppp = SearchS(osn_loc)
            page_loc = ppp.page_base
            # page_loc = osn_loc.add(pppp, text=text)
        case 'searches_dict':
            page_loc = Frame(osn_loc)
    osn_loc.add(page_loc, text=text)
    # return page_loc
