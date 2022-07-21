
import datetime
import pydantic
import rframe
from pydantic import validator
from typing import Literal

from ..base_schemas import XeDoc
from ..._settings import settings

DETECTOR_TYPE = Literal['tpc','neutron_veto','muon_veto']

class BasePmtData(XeDoc):
    _ALIAS = ""
    _CATEGORY = "pmt_data"

    @classmethod
    def default_database_name(cls):
        return 'xepmts'
