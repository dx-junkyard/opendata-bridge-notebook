class EmergencyEvacuationSite:
    """
    指定緊急避難場所を表すクラス

    Attributes:
        local_gov_code (str): 全国地方公共団体コード。6桁の数字で構成される。
        id (str): 避難場所の一意なID。英数字で構成される。
        name (str): 避難場所の名称。
        name_kana (str): 避難場所の名称（カナ表記）。
        name_english (str): 避難場所の名称（英語表記）。
        address_code (str): 避難場所の所在地を示す全国地方公共団体コード。
        town_id (str): 町字ID。
        address (str): 避難場所の住所（連結表記）。
        prefecture (str): 都道府県。
        city (str): 市区町村。
        town (str): 町字。
        building_info (str): 建物名等(方書)。
        latitude (float): 緯度。
        longitude (float): 経度。
        altitude (float): 標高。
        phone_number (str): 連絡先電話番号。
        extension_number (str): 内線番号。
        email_address (str): メールアドレス。
        form_url (str): WebフォームのURL。
        postal_code (str): 郵便番号。
        city_code (str): 市区町村コード。
        disaster_flood (str): 洪水に対する災害対応。
        disaster_landslide (str): 崖崩れ、土石流及び地滑りに対する災害対応。
        disaster_storm_surge (str): 高潮に対する災害対応。
        disaster_earthquake (str): 地震に対する災害対応。
        disaster_tsunami (str): 津波に対する災害対応。
        disaster_large_fire (str): 大規模な火事に対する災害対応。
        disaster_inland_water_flooding (str): 内水氾濫に対する災害対応。
        disaster_volcanic_phenomenon (str): 火山現象に対する災害対応。
        overlap_with_shelter (str): 指定避難所との重複。
        capacity (int): 想定収容人数。
        target_communities (list): 対象となる町会・自治会。
        url (str): 避難場所の公式ウェブサイトURL。
        image_url (str): 避難場所の画像URL。
        image_license (str): 画像ライセンス。
        notes (str): 備考。
    """

    def __init__(
        self,
        local_gov_code,
        id,
        name,
        name_kana,
        name_english,
        address_code,
        town_id,
        address,
        prefecture,
        city,
        town,
        building_info,
        latitude,
        longitude,
        altitude,
        phone_number,
        extension_number,
        email_address,
        form_url,
        postal_code,
        city_code,
        disaster_flood,
        disaster_landslide,
        disaster_storm_surge,
        disaster_earthquake,
        disaster_tsunami,
        disaster_large_fire,
        disaster_inland_water_flooding,
        disaster_volcanic_phenomenon,
        overlap_with_shelter,
        capacity,
        target_communities,
        url,
        image_url,
        image_license,
        notes,
    ):
        self.local_gov_code = local_gov_code
        self.id = id
        self.name = name
        self.name_kana = name_kana
        self.name_english = name_english
        self.address_code = address_code
        self.town_id = town_id
        self.address = address
        self.prefecture = prefecture
        self.city = city
        self.town = town
        self.building_info = building_info
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.phone_number = phone_number
        self.extension_number = extension_number
        self.email_address = email_address
        self.form_url = form_url
        self.postal_code = postal_code
        self.city_code = city_code
        self.disaster_flood = disaster_flood
        self.disaster_landslide = disaster_landslide
        self.disaster_storm_surge = disaster_storm_surge
        self.disaster_earthquake = disaster_earthquake
        self.disaster_tsunami = disaster_tsunami
        self.disaster_large_fire = disaster_large_fire
        self.disaster_inland_water_flooding = disaster_inland_water_flooding
        self.disaster_volcanic_phenomenon = disaster_volcanic_phenomenon
        self.overlap_with_shelter = overlap_with_shelter
        self.capacity = capacity
        self.target_communities = target_communities
        self.url = url
        self.image_url = image_url
        self.image_license = image_license
        self.notes = notes

    def to_dict(self) -> dict:
        """
        クラスのインスタンスを日本語のキーを持つ辞書に変換して返却する

        return:
            dict: 指定緊急避難場所の情報を日本語のキーを持つ辞書に変換したもの
        """
        return {
            '全国地方公共団体コード': self.local_gov_code,
            'ID': self.id,
            '名称': self.name,
            '名称_カナ': self.name_kana,
            '名称_英字': self.name_english,
            '所在地_全国地方公共団体コード': self.address_code,
            '町字ID': self.town_id,
            '所在地_連結表記': self.address,
            '所在地_都道府県': self.prefecture,
            '所在地_市区町村': self.city,
            '所在地_町字': self.town,
            '所在地_番地以下': None,  # CSVデータに含まれないためNone
            '建物名等(方書)': self.building_info,
            '緯度': self.latitude,
            '経度': self.longitude,
            '標高': self.altitude,
            '電話番号': self.phone_number,
            '内線番号': self.extension_number,
            '連絡先メールアドレス': self.email_address,
            '連絡先FormURL': self.form_url,
            '連絡先備考（その他、SNSなど）': None,  # CSVデータに含まれないためNone
            '郵便番号': self.postal_code,
            '市区町村コード': self.city_code,
            '地方公共団体名': None,  # CSVデータに含まれないためNone
            '災害種別_洪水': self.disaster_flood,
            '災害種別_崖崩れ、土石流及び地滑り': self.disaster_landslide,
            '災害種別_高潮': self.disaster_storm_surge,
            '災害種別_地震': self.disaster_earthquake,
            '災害種別_津波': self.disaster_tsunami,
            '災害種別_大規模な火事': self.disaster_large_fire,
            '災害種別_内水氾濫': self.disaster_inland_water_flooding,
            '災害種別_火山現象': self.disaster_volcanic_phenomenon,
            '指定避難所との重複': self.overlap_with_shelter,
            '想定収容人数': self.capacity,
            '対象となる町会・自治会': self.target_communities,
            'URL': self.url,
            '画像': None,  # CSVデータに含まれないためNone
            '画像_ライセンス': self.image_license,
            '備考': self.notes
        }
