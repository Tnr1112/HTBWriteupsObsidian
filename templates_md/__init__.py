

#imports templates
from .index_template import get_index_template
from .recon_template import get_recon_template
from .exploitation_template import get_exploitation_template
from .post_exploitation_template import get_post_exploitation_template

from .Mio.index_template import get_index_template_mio
from .Mio.loot_template import get_loot_template_mio
from .Mio.commonEnumeration_template import get_common_enumeration_template_mio
from .Mio.webpages_template import get_webpages_template_mio

#imports machine info
from .template_char_user_rating import get_template_char_user_rating
from .template_chart_radar import get_template_chart_radar
from .machine_template import get_machine_template

