"""
# S2(x,y) correction codes
**Jianyu Long (jylong@uchicago.edu)**

Time dependence of Extraction Efficiency generated from Kr83m calibration data and propagated to all runs. As discussed in [this note](https://xe1t-wiki.lngs.infn.it/doku.php?id=jlong:sr0_ramp_up_kr_se_study#updated_correction_maps) the extraction efficiency seems have a strong correlation with time delay from the nearest ramp up. This dependence should be regarded together with Single Electron Gain evolution (also in that note). 

## Brief info

- This correction is generated by interpolating EE as a function of time delay from the ramp up for Kr83m calibration runs during 5.3.2021 and 5.15.2021
- V0 is just for qualitative purpose and Straxen algorithm test
- The json file contains two meaningful fields: `timestamps` and `correction`: `timestamps` are simply starting time for all available runs; `correction` are the associated correction coefficients. 

"""
import rframe

from .base_corrections import TimeSampledCorrection
from ..constants import PARTITION


class RelExtractionEff(TimeSampledCorrection):
    _ALIAS = "rel_extraction_effs"

    partition: PARTITION = rframe.Index(default='all_tpc')
    value: float
