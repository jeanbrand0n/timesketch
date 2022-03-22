# Copyright 2018 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Emoji codepoint definitions.

See https://emojipedia.org for list of available unicode emojis.
"""

from __future__ import unicode_literals

import collections


emoji = collections.namedtuple("emoji", "code help")


EMOJI_MAP = {
    "CAMERA": emoji("&#x1F4F7", "Screenshot activity"),
    "FISHING_POLE": emoji("&#x1F3A3", "Phishing"),
    "ID_BUTTON": emoji("&#x1F194", "Account ID"),
    "LINK": emoji("&#x1F517", "Events Linked"),
    "LOCK": emoji("&#x1F512", "Logon activity"),
    "LOCOMOTIVE": emoji("&#x1F682", "Execution activity"),
    "MAGNIFYING_GLASS": emoji("&#x1F50E", "Search related activity"),
    "SATELLITE": emoji("&#x1F4E1", "Domain activity"),
    "SCREEN": emoji("&#x1F5B5", "Screensaver activity"),
    "SKULL": emoji("&#x1F480;", "Threat intel match"),
    "SKULL_CROSSBONE": emoji("&#x2620", "Suspicious entry"),
    "SLEEPING_FACE": emoji("&#x1F634", "Activity outside of regular hours"),
    "UNLOCK": emoji("&#x1F513", "Logoff activity"),
    "WASTEBASKET": emoji("&#x1F5D1", "Deletion activity"),
    "FLAG_AC": emoji("&#x1F1E6&#x1F1E8", "Ascension Island"),
    "FLAG_AD": emoji("&#x1F1E6&#x1F1E9", "Andorra"),
    "FLAG_AE": emoji("&#x1F1E6&#x1F1EA", "United Arab Emirates"),
    "FLAG_AF": emoji("&#x1F1E6&#x1F1EB", "Afghanistan"),
    "FLAG_AG": emoji("&#x1F1E6&#x1F1EC", "Antigua & Barbuda"),
    "FLAG_AI": emoji("&#x1F1E6&#x1F1EE", "Anguilla"),
    "FLAG_AL": emoji("&#x1F1E6&#x1F1F1", "Albania"),
    "FLAG_AM": emoji("&#x1F1E6&#x1F1F2", "Armenia"),
    "FLAG_AO": emoji("&#x1F1E6&#x1F1F4", "Angola"),
    "FLAG_AQ": emoji("&#x1F1E6&#x1F1F6", "Antarctica"),
    "FLAG_AR": emoji("&#x1F1E6&#x1F1F7", "Argentina"),
    "FLAG_AS": emoji("&#x1F1E6&#x1F1F8", "American Samoa"),
    "FLAG_AT": emoji("&#x1F1E6&#x1F1F9", "Austria"),
    "FLAG_AU": emoji("&#x1F1E6&#x1F1FA", "Australia"),
    "FLAG_AW": emoji("&#x1F1E6&#x1F1FC", "Aruba"),
    "FLAG_AX": emoji("&#x1F1E6&#x1F1FD", "Åland Islands"),
    "FLAG_AZ": emoji("&#x1F1E6&#x1F1FF", "Azerbaijan"),
    "FLAG_BA": emoji("&#x1F1E7&#x1F1E6", "Bosnia & Herzegovina"),
    "FLAG_BB": emoji("&#x1F1E7&#x1F1E7", "Barbados"),
    "FLAG_BD": emoji("&#x1F1E7&#x1F1E9", "Bangladesh"),
    "FLAG_BE": emoji("&#x1F1E7&#x1F1EA", "Belgium"),
    "FLAG_BF": emoji("&#x1F1E7&#x1F1EB", "Burkina Faso"),
    "FLAG_BG": emoji("&#x1F1E7&#x1F1EC", "Bulgaria"),
    "FLAG_BH": emoji("&#x1F1E7&#x1F1ED", "Bahrain"),
    "FLAG_BI": emoji("&#x1F1E7&#x1F1EE", "Burundi"),
    "FLAG_BJ": emoji("&#x1F1E7&#x1F1EF", "Benin"),
    "FLAG_BL": emoji("&#x1F1E7&#x1F1F1", "St. Barthélemy"),
    "FLAG_BM": emoji("&#x1F1E7&#x1F1F2", "Bermuda"),
    "FLAG_BN": emoji("&#x1F1E7&#x1F1F3", "Brunei"),
    "FLAG_BO": emoji("&#x1F1E7&#x1F1F4", "Bolivia"),
    "FLAG_BQ": emoji("&#x1F1E7&#x1F1F6", "Caribbean Netherlands"),
    "FLAG_BR": emoji("&#x1F1E7&#x1F1F7", "Brazil"),
    "FLAG_BS": emoji("&#x1F1E7&#x1F1F8", "Bahamas"),
    "FLAG_BT": emoji("&#x1F1E7&#x1F1F9", "Bhutan"),
    "FLAG_BV": emoji("&#x1F1E7&#x1F1FB", "Bouvet Island"),
    "FLAG_BW": emoji("&#x1F1E7&#x1F1FC", "Botswana"),
    "FLAG_BY": emoji("&#x1F1E7&#x1F1FE", "Belarus"),
    "FLAG_BZ": emoji("&#x1F1E7&#x1F1FF", "Belize"),
    "FLAG_CA": emoji("&#x1F1E8&#x1F1E6", "Canada"),
    "FLAG_CC": emoji("&#x1F1E8&#x1F1E8", "Cocos (Keeling) Islands"),
    "FLAG_CD": emoji("&#x1F1E8&#x1F1E9", "Congo - Kinshasa"),
    "FLAG_CF": emoji("&#x1F1E8&#x1F1EB", "Central African Republic"),
    "FLAG_CG": emoji("&#x1F1E8&#x1F1EC", "Congo - Brazzaville"),
    "FLAG_CH": emoji("&#x1F1E8&#x1F1ED", "Switzerland"),
    "FLAG_CI": emoji("&#x1F1E8&#x1F1EE", "Côte d’Ivoire"),
    "FLAG_CK": emoji("&#x1F1E8&#x1F1F0", "Cook Islands"),
    "FLAG_CL": emoji("&#x1F1E8&#x1F1F1", "Chile"),
    "FLAG_CM": emoji("&#x1F1E8&#x1F1F2", "Cameroon"),
    "FLAG_CN": emoji("&#x1F1E8&#x1F1F3", "China"),
    "FLAG_CO": emoji("&#x1F1E8&#x1F1F4", "Colombia"),
    "FLAG_CP": emoji("&#x1F1E8&#x1F1F5", "Clipperton Island"),
    "FLAG_CR": emoji("&#x1F1E8&#x1F1F7", "Costa Rica"),
    "FLAG_CU": emoji("&#x1F1E8&#x1F1FA", "Cuba"),
    "FLAG_CV": emoji("&#x1F1E8&#x1F1FB", "Cape Verde"),
    "FLAG_CW": emoji("&#x1F1E8&#x1F1FC", "Curaçao"),
    "FLAG_CX": emoji("&#x1F1E8&#x1F1FD", "Christmas Island"),
    "FLAG_CY": emoji("&#x1F1E8&#x1F1FE", "Cyprus"),
    "FLAG_CZ": emoji("&#x1F1E8&#x1F1FF", "Czechia"),
    "FLAG_DE": emoji("&#x1F1E9&#x1F1EA", "Germany"),
    "FLAG_DG": emoji("&#x1F1E9&#x1F1EC", "Diego Garcia"),
    "FLAG_DJ": emoji("&#x1F1E9&#x1F1EF", "Djibouti"),
    "FLAG_DK": emoji("&#x1F1E9&#x1F1F0", "Denmark"),
    "FLAG_DM": emoji("&#x1F1E9&#x1F1F2", "Dominica"),
    "FLAG_DO": emoji("&#x1F1E9&#x1F1F4", "Dominican Republic"),
    "FLAG_DZ": emoji("&#x1F1E9&#x1F1FF", "Algeria"),
    "FLAG_EA": emoji("&#x1F1EA&#x1F1E6", "Ceuta & Melilla"),
    "FLAG_EC": emoji("&#x1F1EA&#x1F1E8", "Ecuador"),
    "FLAG_EE": emoji("&#x1F1EA&#x1F1EA", "Estonia"),
    "FLAG_EG": emoji("&#x1F1EA&#x1F1EC", "Egypt"),
    "FLAG_EH": emoji("&#x1F1EA&#x1F1ED", "Western Sahara"),
    "FLAG_ER": emoji("&#x1F1EA&#x1F1F7", "Eritrea"),
    "FLAG_ES": emoji("&#x1F1EA&#x1F1F8", "Spain"),
    "FLAG_ET": emoji("&#x1F1EA&#x1F1F9", "Ethiopia"),
    "FLAG_EU": emoji("&#x1F1EA&#x1F1FA", "European Union"),
    "FLAG_FI": emoji("&#x1F1EB&#x1F1EE", "Finland"),
    "FLAG_FJ": emoji("&#x1F1EB&#x1F1EF", "Fiji"),
    "FLAG_FK": emoji("&#x1F1EB&#x1F1F0", "Falkland Islands"),
    "FLAG_FM": emoji("&#x1F1EB&#x1F1F2", "Micronesia"),
    "FLAG_FO": emoji("&#x1F1EB&#x1F1F4", "Faroe Islands"),
    "FLAG_FR": emoji("&#x1F1EB&#x1F1F7", "France"),
    "FLAG_GA": emoji("&#x1F1EC&#x1F1E6", "Gabon"),
    "FLAG_GB": emoji("&#x1F1EC&#x1F1E7", "United Kingdom"),
    "FLAG_GD": emoji("&#x1F1EC&#x1F1E9", "Grenada"),
    "FLAG_GE": emoji("&#x1F1EC&#x1F1EA", "Georgia"),
    "FLAG_GF": emoji("&#x1F1EC&#x1F1EB", "French Guiana"),
    "FLAG_GG": emoji("&#x1F1EC&#x1F1EC", "Guernsey"),
    "FLAG_GH": emoji("&#x1F1EC&#x1F1ED", "Ghana"),
    "FLAG_GI": emoji("&#x1F1EC&#x1F1EE", "Gibraltar"),
    "FLAG_GL": emoji("&#x1F1EC&#x1F1F1", "Greenland"),
    "FLAG_GM": emoji("&#x1F1EC&#x1F1F2", "Gambia"),
    "FLAG_GN": emoji("&#x1F1EC&#x1F1F3", "Guinea"),
    "FLAG_GP": emoji("&#x1F1EC&#x1F1F5", "Guadeloupe"),
    "FLAG_GQ": emoji("&#x1F1EC&#x1F1F6", "Equatorial Guinea"),
    "FLAG_GR": emoji("&#x1F1EC&#x1F1F7", "Greece"),
    "FLAG_GS": emoji("&#x1F1EC&#x1F1F8", "South Georgia & South Sandwich Islands"),
    "FLAG_GT": emoji("&#x1F1EC&#x1F1F9", "Guatemala"),
    "FLAG_GU": emoji("&#x1F1EC&#x1F1FA", "Guam"),
    "FLAG_GW": emoji("&#x1F1EC&#x1F1FC", "Guinea-Bissau"),
    "FLAG_GY": emoji("&#x1F1EC&#x1F1FE", "Guyana"),
    "FLAG_HK": emoji("&#x1F1ED&#x1F1F0", "Hong Kong SAR China"),
    "FLAG_HM": emoji("&#x1F1ED&#x1F1F2", "Heard & McDonald Islands"),
    "FLAG_HN": emoji("&#x1F1ED&#x1F1F3", "Honduras"),
    "FLAG_HR": emoji("&#x1F1ED&#x1F1F7", "Croatia"),
    "FLAG_HT": emoji("&#x1F1ED&#x1F1F9", "Haiti"),
    "FLAG_HU": emoji("&#x1F1ED&#x1F1FA", "Hungary"),
    "FLAG_IC": emoji("&#x1F1EE&#x1F1E8", "Canary Islands"),
    "FLAG_ID": emoji("&#x1F1EE&#x1F1E9", "Indonesia"),
    "FLAG_IE": emoji("&#x1F1EE&#x1F1EA", "Ireland"),
    "FLAG_IL": emoji("&#x1F1EE&#x1F1F1", "Israel"),
    "FLAG_IM": emoji("&#x1F1EE&#x1F1F2", "Isle of Man"),
    "FLAG_IN": emoji("&#x1F1EE&#x1F1F3", "India"),
    "FLAG_IO": emoji("&#x1F1EE&#x1F1F4", "British Indian Ocean Territory"),
    "FLAG_IQ": emoji("&#x1F1EE&#x1F1F6", "Iraq"),
    "FLAG_IR": emoji("&#x1F1EE&#x1F1F7", "Iran"),
    "FLAG_IS": emoji("&#x1F1EE&#x1F1F8", "Iceland"),
    "FLAG_IT": emoji("&#x1F1EE&#x1F1F9", "Italy"),
    "FLAG_JE": emoji("&#x1F1EF&#x1F1EA", "Jersey"),
    "FLAG_JM": emoji("&#x1F1EF&#x1F1F2", "Jamaica"),
    "FLAG_JO": emoji("&#x1F1EF&#x1F1F4", "Jordan"),
    "FLAG_JP": emoji("&#x1F1EF&#x1F1F5", "Japan"),
    "FLAG_KE": emoji("&#x1F1F0&#x1F1EA", "Kenya"),
    "FLAG_KG": emoji("&#x1F1F0&#x1F1EC", "Kyrgyzstan"),
    "FLAG_KH": emoji("&#x1F1F0&#x1F1ED", "Cambodia"),
    "FLAG_KI": emoji("&#x1F1F0&#x1F1EE", "Kiribati"),
    "FLAG_KM": emoji("&#x1F1F0&#x1F1F2", "Comoros"),
    "FLAG_KN": emoji("&#x1F1F0&#x1F1F3", "St. Kitts & Nevis"),
    "FLAG_KP": emoji("&#x1F1F0&#x1F1F5", "North Korea"),
    "FLAG_KR": emoji("&#x1F1F0&#x1F1F7", "South Korea"),
    "FLAG_KW": emoji("&#x1F1F0&#x1F1FC", "Kuwait"),
    "FLAG_KY": emoji("&#x1F1F0&#x1F1FE", "Cayman Islands"),
    "FLAG_KZ": emoji("&#x1F1F0&#x1F1FF", "Kazakhstan"),
    "FLAG_LA": emoji("&#x1F1F1&#x1F1E6", "Laos"),
    "FLAG_LB": emoji("&#x1F1F1&#x1F1E7", "Lebanon"),
    "FLAG_LC": emoji("&#x1F1F1&#x1F1E8", "St. Lucia"),
    "FLAG_LI": emoji("&#x1F1F1&#x1F1EE", "Liechtenstein"),
    "FLAG_LK": emoji("&#x1F1F1&#x1F1F0", "Sri Lanka"),
    "FLAG_LR": emoji("&#x1F1F1&#x1F1F7", "Liberia"),
    "FLAG_LS": emoji("&#x1F1F1&#x1F1F8", "Lesotho"),
    "FLAG_LT": emoji("&#x1F1F1&#x1F1F9", "Lithuania"),
    "FLAG_LU": emoji("&#x1F1F1&#x1F1FA", "Luxembourg"),
    "FLAG_LV": emoji("&#x1F1F1&#x1F1FB", "Latvia"),
    "FLAG_LY": emoji("&#x1F1F1&#x1F1FE", "Libya"),
    "FLAG_MA": emoji("&#x1F1F2&#x1F1E6", "Morocco"),
    "FLAG_MC": emoji("&#x1F1F2&#x1F1E8", "Monaco"),
    "FLAG_MD": emoji("&#x1F1F2&#x1F1E9", "Moldova"),
    "FLAG_ME": emoji("&#x1F1F2&#x1F1EA", "Montenegro"),
    "FLAG_MF": emoji("&#x1F1F2&#x1F1EB", "St. Martin"),
    "FLAG_MG": emoji("&#x1F1F2&#x1F1EC", "Madagascar"),
    "FLAG_MH": emoji("&#x1F1F2&#x1F1ED", "Marshall Islands"),
    "FLAG_MK": emoji("&#x1F1F2&#x1F1F0", "Macedonia"),
    "FLAG_ML": emoji("&#x1F1F2&#x1F1F1", "Mali"),
    "FLAG_MM": emoji("&#x1F1F2&#x1F1F2", "Myanmar (Burma)"),
    "FLAG_MN": emoji("&#x1F1F2&#x1F1F3", "Mongolia"),
    "FLAG_MO": emoji("&#x1F1F2&#x1F1F4", "Macao SAR China"),
    "FLAG_MP": emoji("&#x1F1F2&#x1F1F5", "Northern Mariana Islands"),
    "FLAG_MQ": emoji("&#x1F1F2&#x1F1F6", "Martinique"),
    "FLAG_MR": emoji("&#x1F1F2&#x1F1F7", "Mauritania"),
    "FLAG_MS": emoji("&#x1F1F2&#x1F1F8", "Montserrat"),
    "FLAG_MT": emoji("&#x1F1F2&#x1F1F9", "Malta"),
    "FLAG_MU": emoji("&#x1F1F2&#x1F1FA", "Mauritius"),
    "FLAG_MV": emoji("&#x1F1F2&#x1F1FB", "Maldives"),
    "FLAG_MW": emoji("&#x1F1F2&#x1F1FC", "Malawi"),
    "FLAG_MX": emoji("&#x1F1F2&#x1F1FD", "Mexico"),
    "FLAG_MY": emoji("&#x1F1F2&#x1F1FE", "Malaysia"),
    "FLAG_MZ": emoji("&#x1F1F2&#x1F1FF", "Mozambique"),
    "FLAG_NA": emoji("&#x1F1F3&#x1F1E6", "Namibia"),
    "FLAG_NC": emoji("&#x1F1F3&#x1F1E8", "New Caledonia"),
    "FLAG_NE": emoji("&#x1F1F3&#x1F1EA", "Niger"),
    "FLAG_NF": emoji("&#x1F1F3&#x1F1EB", "Norfolk Island"),
    "FLAG_NG": emoji("&#x1F1F3&#x1F1EC", "Nigeria"),
    "FLAG_NI": emoji("&#x1F1F3&#x1F1EE", "Nicaragua"),
    "FLAG_NL": emoji("&#x1F1F3&#x1F1F1", "Netherlands"),
    "FLAG_NO": emoji("&#x1F1F3&#x1F1F4", "Norway"),
    "FLAG_NP": emoji("&#x1F1F3&#x1F1F5", "Nepal"),
    "FLAG_NR": emoji("&#x1F1F3&#x1F1F7", "Nauru"),
    "FLAG_NU": emoji("&#x1F1F3&#x1F1FA", "Niue"),
    "FLAG_NZ": emoji("&#x1F1F3&#x1F1FF", "New Zealand"),
    "FLAG_OM": emoji("&#x1F1F4&#x1F1F2", "Oman "),
    "FLAG_PA": emoji("&#x1F1F5&#x1F1E6", "Panama"),
    "FLAG_PE": emoji("&#x1F1F5&#x1F1EA", "Peru"),
    "FLAG_PF": emoji("&#x1F1F5&#x1F1EB", "French Polynesia"),
    "FLAG_PG": emoji("&#x1F1F5&#x1F1EC", "Papua New Guinea"),
    "FLAG_PH": emoji("&#x1F1F5&#x1F1ED", "Philippines"),
    "FLAG_PK": emoji("&#x1F1F5&#x1F1F0", "Pakistan"),
    "FLAG_PL": emoji("&#x1F1F5&#x1F1F1", "Poland"),
    "FLAG_PM": emoji("&#x1F1F5&#x1F1F2", "St. Pierre & Miquelon"),
    "FLAG_PN": emoji("&#x1F1F5&#x1F1F3", "Pitcairn Islands"),
    "FLAG_PR": emoji("&#x1F1F5&#x1F1F7", "Puerto Rico"),
    "FLAG_PS": emoji("&#x1F1F5&#x1F1F8", "Palestinian Territories"),
    "FLAG_PT": emoji("&#x1F1F5&#x1F1F9", "Portugal"),
    "FLAG_PW": emoji("&#x1F1F5&#x1F1FC", "Palau"),
    "FLAG_PY": emoji("&#x1F1F5&#x1F1FE", "Paraguay"),
    "FLAG_QA": emoji("&#x1F1F6&#x1F1E6", "Qatar"),
    "FLAG_RE": emoji("&#x1F1F7&#x1F1EA", "Réunion"),
    "FLAG_RO": emoji("&#x1F1F7&#x1F1F4", "Romania"),
    "FLAG_RS": emoji("&#x1F1F7&#x1F1F8", "Serbia"),
    "FLAG_RU": emoji("&#x1F1F7&#x1F1FA", "Russia"),
    "FLAG_RW": emoji("&#x1F1F7&#x1F1FC", "Rwanda"),
    "FLAG_SA": emoji("&#x1F1F8&#x1F1E6", "Saudi Arabia"),
    "FLAG_SB": emoji("&#x1F1F8&#x1F1E7", "Solomon Islands"),
    "FLAG_SC": emoji("&#x1F1F8&#x1F1E8", "Seychelles"),
    "FLAG_SD": emoji("&#x1F1F8&#x1F1E9", "Sudan"),
    "FLAG_SE": emoji("&#x1F1F8&#x1F1EA", "Sweden"),
    "FLAG_SG": emoji("&#x1F1F8&#x1F1EC", "Singapore"),
    "FLAG_SH": emoji("&#x1F1F8&#x1F1ED", "St. Helena"),
    "FLAG_SI": emoji("&#x1F1F8&#x1F1EE", "Slovenia"),
    "FLAG_SJ": emoji("&#x1F1F8&#x1F1EF", "Svalbard & Jan Mayen"),
    "FLAG_SK": emoji("&#x1F1F8&#x1F1F0", "Slovakia"),
    "FLAG_SL": emoji("&#x1F1F8&#x1F1F1", "Sierra Leone"),
    "FLAG_SM": emoji("&#x1F1F8&#x1F1F2", "San Marino"),
    "FLAG_SN": emoji("&#x1F1F8&#x1F1F3", "Senegal"),
    "FLAG_SO": emoji("&#x1F1F8&#x1F1F4", "Somalia"),
    "FLAG_SR": emoji("&#x1F1F8&#x1F1F7", "Suriname"),
    "FLAG_SS": emoji("&#x1F1F8&#x1F1F8", "South Sudan"),
    "FLAG_ST": emoji("&#x1F1F8&#x1F1F9", "São Tomé & Príncipe"),
    "FLAG_SV": emoji("&#x1F1F8&#x1F1FB", "El Salvador"),
    "FLAG_SX": emoji("&#x1F1F8&#x1F1FD", "Sint Maarten"),
    "FLAG_SY": emoji("&#x1F1F8&#x1F1FE", "Syria"),
    "FLAG_SZ": emoji("&#x1F1F8&#x1F1FF", "Eswatini"),
    "FLAG_TA": emoji("&#x1F1F9&#x1F1E6", "Tristan da Cunha"),
    "FLAG_TC": emoji("&#x1F1F9&#x1F1E8", "Turks & Caicos Islands"),
    "FLAG_TD": emoji("&#x1F1F9&#x1F1E9", "Chad"),
    "FLAG_TF": emoji("&#x1F1F9&#x1F1EB", "French Southern Territories"),
    "FLAG_TG": emoji("&#x1F1F9&#x1F1EC", "Togo"),
    "FLAG_TH": emoji("&#x1F1F9&#x1F1ED", "Thailand"),
    "FLAG_TJ": emoji("&#x1F1F9&#x1F1EF", "Tajikistan"),
    "FLAG_TK": emoji("&#x1F1F9&#x1F1F0", "Tokelau"),
    "FLAG_TL": emoji("&#x1F1F9&#x1F1F1", "Timor-Leste"),
    "FLAG_TM": emoji("&#x1F1F9&#x1F1F2", "Turkmenistan"),
    "FLAG_TN": emoji("&#x1F1F9&#x1F1F3", "Tunisia"),
    "FLAG_TO": emoji("&#x1F1F9&#x1F1F4", "Tonga"),
    "FLAG_TR": emoji("&#x1F1F9&#x1F1F7", "Turkey"),
    "FLAG_TT": emoji("&#x1F1F9&#x1F1F9", "Trinidad & Tobago"),
    "FLAG_TV": emoji("&#x1F1F9&#x1F1FB", "Tuvalu"),
    "FLAG_TW": emoji("&#x1F1F9&#x1F1FC", "Taiwan"),
    "FLAG_TZ": emoji("&#x1F1F9&#x1F1FF", "Tanzania"),
    "FLAG_UA": emoji("&#x1F1FA&#x1F1E6", "Ukraine"),
    "FLAG_UG": emoji("&#x1F1FA&#x1F1EC", "Uganda"),
    "FLAG_UM": emoji("&#x1F1FA&#x1F1F2", "U.S. Outlying Islands"),
    "FLAG_UN": emoji("&#x1F1FA&#x1F1F3", "United Nations"),
    "FLAG_US": emoji("&#x1F1FA&#x1F1F8", "United States"),
    "FLAG_UY": emoji("&#x1F1FA&#x1F1FE", "Uruguay"),
    "FLAG_UZ": emoji("&#x1F1FA&#x1F1FF", "Uzbekistan"),
    "FLAG_VA": emoji("&#x1F1FB&#x1F1E6", "Vatican City"),
    "FLAG_VC": emoji("&#x1F1FB&#x1F1E8", "St. Vincent & Grenadines"),
    "FLAG_VE": emoji("&#x1F1FB&#x1F1EA", "Venezuela"),
    "FLAG_VG": emoji("&#x1F1FB&#x1F1EC", "British Virgin Islands"),
    "FLAG_VI": emoji("&#x1F1FB&#x1F1EE", "U.S. Virgin Islands"),
    "FLAG_VN": emoji("&#x1F1FB&#x1F1F3", "Vietnam"),
    "FLAG_VU": emoji("&#x1F1FB&#x1F1FA", "Vanuatu"),
    "FLAG_WF": emoji("&#x1F1FC&#x1F1EB", "Wallis & Futuna"),
    "FLAG_WS": emoji("&#x1F1FC&#x1F1F8", "Samoa"),
    "FLAG_XK": emoji("&#x1F1FD&#x1F1F0", "Kosovo"),
    "FLAG_YE": emoji("&#x1F1FE&#x1F1EA", "Yemen"),
    "FLAG_YT": emoji("&#x1F1FE&#x1F1F9", "Mayotte"),
    "FLAG_ZA": emoji("&#x1F1FF&#x1F1E6", "South Africa"),
    "FLAG_ZM": emoji("&#x1F1FF&#x1F1F2", "Zambia"),
    "FLAG_ZW": emoji("&#x1F1FF&#x1F1FC", "Zimbabwe"),
}


def get_emoji(name):
    """Returns a Unicode for an emoji given the name or blank if not saved.

    Args:
        name: string with the emoji name.

    Returns:
        Unicode string for the emoji if it exists or a blank string otherwise.
    """
    name_upper = name.upper()
    emoji_object = EMOJI_MAP.get(name_upper)
    if emoji_object:
        return emoji_object.code
    return ""


def get_helper_from_unicode(code):
    """Returns a helper string from an emoji Unicode code point.

    Args:
        code: a Unicode code point for an emoji.

    Returns:
        Helper text as a string or an empty string if emoji is not configured.
    """
    code_upper = code.upper()
    for emoji_object in iter(EMOJI_MAP.values()):
        if code_upper == emoji_object.code.upper():
            return emoji_object.help
    return ""


def get_emojis_as_dict():
    """Returns a dictionary with emoji codes and helper texts.

    Returns:
        Dict with emoji unicode code points as key and helper text as value.
    """
    return {e.code: e.help for e in iter(EMOJI_MAP.values())}
