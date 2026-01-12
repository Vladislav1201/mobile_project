from django.db import models

class PhoneType(models.TextChoices):
    OLD_PHONE = 'old_phone', 'кнопочный телефон'
    SMART = 'smart', 'смартфон'

class OperationSystem(models.TextChoices):
    ANDROID = 'android', 'Android'
    APPLE_IOS = 'apple_ios', 'Apple iOS'
    BLACKBERRY_OS = 'blackberry_os', 'BlackBerry OS'
    HARMONY_OS = 'harmony_os', 'HarmonyOS'
    KAI_OS = 'kaios', 'KaiOS'
    NOKIA_SERIES_30_PLUS = 'nokia_series_30_plus', 'Nokia Series 30+'
    NUCLEUS = 'nucleus', 'Nucleus'
    RTOS = 'rtos', 'RTOS'

class ScreenTechnology(models.TextChoices):
    AMOLED = 'amoled', 'AMOLED'
    IPS = 'ips', 'IPS'
    OLED = 'oled', 'OLED'
    TFT = 'tft', 'TFT'
    PLS = 'pls', 'PLS'
    STN = 'stn', 'STN'

class RefreshRate(models.TextChoices):
    REFRESH_60 = 'refresh_60', '60'
    REFRESH_90 = 'refresh_90', '90'
    REFRESH_120 = 'refresh_120', '120'
    REFRESH_144 = 'refresh_144', '144'
    REFRESH_165 = 'refresh_165', '165'
    REFRESH_185 = 'refresh_185', '185'

class RamSize(models.TextChoices):
    RAM_32_MB = 'ram_32_mb', '32 Мб'
    RAM_512_MB = 'ram_512_mb', '512 Мб'
    RAM_768_MB = 'ram_768_mb', '768 Мб'
    RAM_1_GB = 'ram_1_gb', '1 Гб'
    RAM_1_5_GB = 'ram_1_5_gb', '1,5 Гб'
    RAM_2_GB = 'ram_2_gb', '2 Гб'
    RAM_3_GB = 'ram_3_gb', '3 Гб'
    RAM_4_GB = 'ram_4_gb', '4 Гб'
    RAM_6_GB = 'ram_6_gb', '6 Гб'
    RAM_8_GB = 'ram_8_gb', '8 Гб'
    RAM_12_GB = 'ram_12_gb', '12 Гб'
    RAM_16_GB = 'ram_16_gb', '16 Гб'
    RAM_18_GB = 'ram_18_gb', '18 Гб'
    RAM_20_GB = 'ram_20_gb', '20 Гб'
    RAM_24_GB = 'ram_24_gb', '24 Гб'

class StorageSize(models.TextChoices):
    STORAGE_800_KB = 'storage_800_kb', '800 Кб'
    STORAGE_4_GB = 'storage_4_GB', '4 Гб'
    STORAGE_8_GB = 'storage_8_GB', '8 Гб'
    STORAGE_16_GB = 'storage_16_GB', '16 Гб'
    STORAGE_32_GB = 'storage_32_GB', '4 Гб'
    STORAGE_64_GB = 'storage_64_GB', '64 Гб'
    STORAGE_128_GB = 'storage_128_GB', '128 Гб'
    STORAGE_256_GB = 'storage_256_GB', '256 Гб'
    STORAGE_512_GB = 'storage_512_GB', '512 Гб'
    STORAGE_1_TB = 'storage_1_tb', '1 Tб'
    STORAGE_2_TB = 'storage_2_tb', '2 Tб'

class VideoResolution(models.TextChoices):
    RESOLUTION_1280_720 = 'resolution_1280_720', '1280×720 (30 кадров/с)'
    RESOLUTION_1920_1080_24 = 'resolution_1920_1080_24', '1920×1080 (24 кадров/с)'
    RESOLUTION_1920_1280_30 = 'resolution_1920_1280_30', '1920×1280 (30 кадров/с)'
    RESOLUTION_1920_1280_60 = 'resolution_1920_1280_60', '1920×1280 (60 кадров/с)'
    RESOLUTION_2560_1440 = 'resolution_2560_1440', '2560×1440 (30 кадров/с)'
    RESOLUTION_3840_1920 = 'resolution_3840_1920', '3840×1920 (30 кадров/с)'
    RESOLUTION_3840_2160_60 = 'resolution_3840_2160_60', '3840×2160 (60 кадров/с)'
    RESOLUTION_3840_2160_120 = 'resolution_3840_2160_120', '3840×2160 (120 кадров/с)'
    RESOLUTION_4096_2160 = 'resolution_4096_2160', '4096×2160 (30 кадров/с)'
    RESOLUTION_7680_4320_24 = 'resolution_7680_4320_24', '7680×4320 (24 кадров/с)'
    RESOLUTION_7680_4320_30 = 'resolution_7680_4320_30', '7680×4320 (30 кадров/с)'


class FastCharge(models.TextField):
    FAST_CHARGE_YES = 'fast_charge_yes', '+'
    FAST_CHARGE_NO = 'fast_charge_no', '-'

class MemoryCard(models.TextChoices):
    MEMORY_CARD_YES = 'memory_card_yes', '+'
    MEMORY_CARD_NO = 'memory_card_no', '-'

class SimSlots(models.TextChoices):
    SIM_SLOTS_1 = '1', '1 SIM'
    SIM_SLOTS_2 = '2', '2 SIM'
    SIM_SLOTS_3 = '3', '3 SIM'
    SIM_SLOTS_4 = '4', '4 SIM'

class OSVersion(models.TextChoices):
    ANDROID_4_0 = 'android_4_0', 'Android 4.0 Ice Cream'
    ANDROID_4_1 = 'android_4_1', 'Android 4.1 Jelly Bean'
    ANDROID_4_3 = 'android_4_3', 'Android 4.3 Jelly Bean'
    ANDROID_4_4 = 'android_4_4', 'Android 4.4 KitKat'
    ANDROID_5_1 = 'android_5_1', 'Android 5.1 Lollipop'
    ANDROID_6_0 = 'android_6_0', 'Android 6.0 Marshmallow'
    ANDROID_7_0 = 'android_7_0', 'Android 7.0 Nougat'
    ANDROID_7_1 = 'android_7_1', 'Android 7.1 Nougat'
    ANDROID_8_0 = 'android_8_0', 'Android 8.0 Oreo'
    ANDROID_8_1 = 'android_8_1', 'Android 8.1 Oreo'
    ANDROID_9 = 'android_9', 'Android 9.0 Pie'
    ANDROID_10 = 'android_10', 'Android 10'
    ANDROID_10_GO = 'android_10_go', 'Android 10 Go Edition'
    ANDROID_11 = 'android_11', 'Android 11'
    ANDROID_11_GO = 'android_11_go', 'Android 11 Go Edition'
    ANDROID_12 = 'android_12', 'Android 12'
    ANDROID_12_GO = 'android_12_go', 'Android 12 Go Edition'
    ANDROID_13 = 'android_13', 'Android 13'
    ANDROID_13_GO = 'android_13_go', 'Android 13 Go Edition'
    ANDROID_14 = 'android_14', 'Android 14'
    ANDROID_14_GO = 'android_14_go', 'Android 14 Go Edition'
    ANDROID_15 = 'android_15', 'Android 15'
    ANDROID_15_GO = 'android_15_go', 'Android 15 Go Edition'
    ANDROID_16 = 'android_16', 'Android 16'

    BLACKBERRY_7 = 'bb_7', 'BlackBerry OS 7.0'
    BLACKBERRY_10 = 'bb_10', 'BlackBerry OS 10.3'

    FLYME = 'flyme', 'Flyme OS'

    HARMONY_2 = 'harmony_2', 'HarmonyOS 2.0'
    HARMONY_4 = 'harmony_4', 'HarmonyOS 4.0'
    HARMONY_4_2 = 'harmony_4_2', 'HarmonyOS 4.2'
    HARMONY_4_3 = 'harmony_4_3', 'HarmonyOS 4.3'
    HARMONY_5 = 'harmony_5', 'HarmonyOS 5.0'
    HARMONY_5_1 = 'harmony_5_1', 'HarmonyOS 5.1'
    HARMONY_6 = 'harmony_6', 'HarmonyOS 6.0'

    IOS_9 = 'ios_9', 'iOS 9'
    IOS_10 = 'ios_10', 'iOS 10'
    IOS_11 = 'ios_11', 'iOS 11'
    IOS_12 = 'ios_12', 'iOS 12'
    IOS_13 = 'ios_13', 'iOS 13'
    IOS_14 = 'ios_14', 'iOS 14'
    IOS_15 = 'ios_15', 'iOS 15'
    IOS_16 = 'ios_16', 'iOS 16'
    IOS_17 = 'ios_17', 'iOS 17'
    IOS_18 = 'ios_18', 'iOS 18'
    IOS_26 = 'ios_26', 'iOS 26'

class CameraMegapixels(models.TextChoices):
    MP_0_08 = '0.08', '0.08 Мп'
    MP_2 = '2', '2 Мп'
    MP_5 = '5', '5 Мп'
    MP_8 = '8', '8 Мп'
    MP_12 = '12', '12 Мп'
    MP_12_2 = '12.2', '12.2 Мп'
    MP_13 = '13', '13 Мп'
    MP_16 = '16', '16 Мп'
    MP_20 = '20', '20 Мп'
    MP_21 = '21', '21 Мп'
    MP_32 = '32', '32 Мп'
    MP_48 = '48', '48 Мп'
    MP_50 = '50', '50 Мп'
    MP_50_3 = '50.3', '50.3 Мп'
    MP_54 = '54', '54 Мп'
    MP_64 = '64', '64 Мп'
    MP_100 = '100', '100 Мп'
    MP_108 = '108', '108 Мп'
    MP_200 = '200', '200 Мп'


class SimType(models.TextChoices):
    PHYSICAL = 'physical', 'Обычная SIM'
    ESIM = 'esim', 'eSIM'
    BOTH = 'both', 'SIM + eSIM'

class Platform(models.TextChoices):
    APPLE = 'apple_a', 'Apple A'
    GOOGLE = 'google_tensor', 'Google Tensor'
    HISILICON = 'hisilicon_kirin', 'HiSilicon Kirin'
    MEDIATEK = 'mediatek', 'MediaTek'
    MEDIATEK_DIMENSITY = 'mediatek_dimensity', 'MediaTek Dimensity'
    MEDIATEK_HELIO = 'mediatek_helio', 'MediaTek Helio'
    QUALCOMM_DRAGONWING = 'qualcomm_dragonwing', 'Qualcomm Dragonwing'
    QUALCOMM_SNAPDRAGON = 'qualcomm_snapdragon', 'Qualcomm Snapdragon'
    SAMSUNG_EXYNOS = 'samsung_exynos', 'Samsung Exynos'
    SPREADTRUM = 'spreadtrum', 'Spreadtrum'
    UNISOC = 'unisoc', 'UniSoC'
    UNISOC_TIGER = 'unisoc_tiger', 'UniSoC Tiger'
    XIAOMI = 'xiaomi_xring', 'Xiaomi Xring'

class CpuCores(models.TextChoices):
    TWO = '2', '2'
    FOUR = '4', '4'
    FOUR_1_3 = '4_1_3', '4 (1+3)'
    FOUR_2_2 = '4_2_2', '4 (2+2)'
    SIX_2_4 = '6_2_4', '6 (2+4)'
    SIX_3_3 = '6_3_3', '6 (3+3)'
    EIGHT = '8', '8'
    EIGHT_1_1_6 = '8_1_1_6', '8 (1+1+6)'
    EIGHT_1_2_2_3 = '8_1_2_2_3', '8 (1+2+2+3)'
    EIGHT_1_3_2_2 = '8_1_3_2_2', '8 (1+3+2+2)'
    EIGHT_1_3_4 = '8_1_3_4', '8 (1+3+4)'
    EIGHT_1_4_3 = '8_1_4_3', '8 (1+4+3)'
    EIGHT_1_5_2 = '8_1_5_2', '8 (1+5+2)'
    EIGHT_2_2_4 = '8_2_2_4', '8 (2+2+4)'
    EIGHT_2_6 = '8_2_6', '8 (2+6)'
    EIGHT_4_4 = '8_4_4', '8 (4+4)'
    NINE_1_4_4 = '9_1_4_4', '9 (1+4+4)'
    TEN_1_2_3_4 = '10_1_2_3_4', '10 (1+2+3+4)'
    TEN_1_2_5_2 = '10_1_2_5_2', '10 (1+2+5+2)'
    TEN_2_4_2_2 = '10_2_4_2_2', '10 (2+4+2+2)'
    TWELVE_2_6_4 = '12_2_6_4', '12 (2+6+4)'

class ProcessTechnology(models.TextChoices):
    NM_3 = '3nm', '3 нм'
    NM_4 = '4nm', '4 нм'
    NM_5 = '5nm', '5 нм'
    NM_6 = '6nm', '6 нм'
    NM_7 = '7nm', '7 нм'
    NM_8 = '8nm', '8 нм'
    NM_10 = '10nm', '10 нм'
    NM_11 = '11nm', '11 нм'
    NM_12 = '12nm', '12 нм'
    NM_14 = '14nm', '14 нм'
    NM_16 = '16nm', '16 нм'
    NM_20 = '20nm', '20 нм'
    NM_28 = '28nm', '28 нм'

class BodyConstruction(models.TextChoices):
    MONOBLOCK = 'monoblock', 'моноблок'
    FLIP = 'flip', 'со складным экраном (flip)'
    FOLD = 'fold', 'со складным экраном (fold)'
    TRIFOLD = 'trifold', 'со складным экраном (trifold)'
    FOLD_GENERIC = 'fold_generic', 'со складным экраном'

class FrameMaterial(models.TextChoices):
    GENERIC = 'generic', 'материал рамки'
    ALUMINUM = 'aluminum', 'алюминий'
    CERAMIC = 'ceramic', 'керамика'
    MAGNESIUM = 'magnesium', 'магниевый сплав'
    METAL = 'metal', 'металл'
    PLASTIC = 'plastic', 'пластик'
    RUBBER = 'rubber', 'резина'
    GLASS = 'glass', 'стекло'
    FIBERGLASS = 'fiberglass', 'стекловолокно'
    TITANIUM = 'titanium', 'титан'
    FABRIC = 'fabric', 'тканевое покрытие'

class BackCoverMaterial(models.TextChoices):
    CERAMIC = 'ceramic', 'керамика'
    LEATHER = 'leather', 'кожа'
    METAL = 'metal', 'металл'
    PLASTIC = 'plastic', 'пластик'
    POLYMER_LEATHER = 'polymer_leather', 'полимерная кожа'
    GLASS = 'glass', 'стекло'
    FIBERGLASS = 'fiberglass', 'стекловолокно'

class BackCoverColor(models.TextChoices):
    BEIGE = 'beige', 'бежевый'
    WHITE = 'white', 'белый'
    TURQUOISE = 'turquoise', 'бирюзовый'
    BORDEAUX = 'bordeaux', 'бордовый'
    BRONZE = 'bronze', 'бронзовый'
    BLUE = 'blue', 'голубой'
    YELLOW = 'yellow', 'желтый'
    GREEN = 'green', 'зеленый'
    GOLD = 'gold', 'золотистый'
    CAMOUFLAGE = 'camouflage', 'камуфляж'
    CORAL = 'coral', 'коралловый'
    BROWN = 'brown', 'коричневый'
    RED = 'red', 'красный'
    COPPER = 'copper', 'медный'
    MINT = 'mint', 'мятный'
    ORANGE = 'orange', 'оранжевый'
    PEARL = 'pearl', 'перламутровый'
    PEACH = 'peach', 'персиковый'
    PINK = 'pink', 'розовый'
    LIGHT_GREEN = 'light_green', 'светло-зеленый'
    LIGHT_GRAY = 'light_gray', 'светло-серый'
    LIGHT_BLUE = 'light_blue', 'светло-синий'
    SILVER = 'silver', 'серебристый'
    GRAY = 'gray', 'серый'
    DARK_BLUE = 'dark_blue', 'синий'
    LILAC = 'lilac', 'сиреневый'
    DARK_GREEN = 'dark_green', 'темно-зеленый'
    DARK_RED = 'dark_red', 'темно-красный'
    DARK_GRAY = 'dark_gray', 'темно-серый'
    DARK_BLUE_2 = 'dark_blue_2', 'темно-синий'
    TITANIUM = 'titanium', 'титановый'
    PURPLE = 'purple', 'фиолетовый'
    BLACK = 'black', 'черный'

class OpticalZoom(models.TextChoices):
    ZOOM_2_5X = '2_5x', '2.5X'
    ZOOM_2_5X_PLUS = '2_5x_plus', '2.5X (на увеличение)'
    ZOOM_2_6X_PLUS = '2_6x_plus', '2.6X (на увеличение)'
    ZOOM_2_7X_PLUS = '2_7x_plus', '2.7X (на увеличение)'
    ZOOM_2X = '2x', '2X'
    ZOOM_2X_PLUS = '2x_plus', '2X (на увеличение)'
    ZOOM_3X = '3x', '3X'
    ZOOM_3_2X = '3_2x', '3.2X'
    ZOOM_3_3X = '3_3x', '3.3X'
    ZOOM_3_4X = '3_4x', '3.4X'
    ZOOM_3_5X = '3_5x', '3.5X'
    ZOOM_3_5X_PLUS = '3_5x_plus', '3.5X (на увеличение)'
    ZOOM_3_7X = '3_7x', '3.7X'
    ZOOM_3_7X_PLUS = '3_7x_plus', '3.7X (на увеличение)'
    ZOOM_4X = '4x', '4X'
    ZOOM_4_3X = '4_3x', '4.3X'
    ZOOM_4_4X = '4_4x', '4.4X'
    ZOOM_4X_SPEC = '4x_spec', '4X (2X на увеличение, 2X на уменьшение)'
    ZOOM_40X = '40x', '40X'
    ZOOM_5X = '5x', '5X'
    ZOOM_5_2X = '5_2x', '5.2X'
    ZOOM_5_5X = '5_5x', '5.5X (на увеличение)'
    ZOOM_5X_SPEC = '5x_spec', '5X (3X на увеличение, 2X на уменьшение)'
    ZOOM_5X_PLUS = '5x_plus', '5X (на увеличение)'
    ZOOM_6X = '6x', '6X'
    ZOOM_6_2X = '6_2x', '6.2X (на увеличение)'
    ZOOM_7X = '7x', '7X'
    ZOOM_7_1X = '7_1x', '7.1X'
    ZOOM_7X_SPEC = '7x_spec', '7X (5X на увеличение, 2X на уменьшение)'
    ZOOM_9X = '9x', '9X'
    ZOOM_9_4X = '9_4x', '9.4X'
    ZOOM_10X = '10x', '10X'
    ZOOM_10X_SPEC = '10x_spec', '10X (8X на увеличение, 2X на уменьшение)'

class MainCameraAperture(models.TextChoices):
    F_1_4 = 'f_1_4', 'f/1.4'
    F_1_4_2_0 = 'f_1_4_2_0', 'f/1.4 - f/2.0'
    F_1_4_4_0 = 'f_1_4_4_0', 'f/1.4 - f/4.0'
    F_1_5 = 'f_1_5', 'f/1.5'
    F_1_6 = 'f_1_6', 'f/1.6'
    F_1_7 = 'f_1_7', 'f/1.7'
    F_1_8 = 'f_1_8', 'f/1.8'
    F_1_9 = 'f_1_9', 'f/1.9'
    F_1_44 = 'f_1_44', 'f/1.44'
    F_1_57 = 'f_1_57', 'f/1.57'
    F_1_59 = 'f_1_59', 'f/1.59'
    F_1_59_4_0 = 'f_1_59_4_0', 'f/1.59 - f/4.0'
    F_1_62 = 'f_1_62', 'f/1.62'
    F_1_63 = 'f_1_63', 'f/1.63'
    F_1_65 = 'f_1_65', 'f/1.65'
    F_1_67 = 'f_1_67', 'f/1.67'
    F_1_68 = 'f_1_68', 'f/1.68'
    F_1_69 = 'f_1_69', 'f/1.69'
    F_1_75 = 'f_1_75', 'f/1.75'
    F_1_77 = 'f_1_77', 'f/1.77'
    F_1_78 = 'f_1_78', 'f/1.78'
    F_1_79 = 'f_1_79', 'f/1.79'
    F_1_85 = 'f_1_85', 'f/1.85'
    F_1_88 = 'f_1_88', 'f/1.88'
    F_1_89 = 'f_1_89', 'f/1.89'
    F_1_95 = 'f_1_95', 'f/1.95'
    F_2_0 = 'f_2_0', 'f/2.0'
    F_2_2 = 'f_2_2', 'f/2.2'
    F_2_4 = 'f_2_4', 'f/2.4'
    F_2_8 = 'f_2_8', 'f/2.8'
    F_2_45 = 'f_2_45', 'f/2.45'

class BluetoothAudioCodecs(models.TextChoices):
    AAC = 'aac', 'AAC'
    APTX = 'aptx', 'aptX'
    APTX_ADAPTIVE = 'aptx_adaptive', 'aptX Adaptive'
    APTX_HD = 'aptx_hd', 'aptX HD'
    APTX_LL = 'aptx_ll', 'aptX LL (aptX Lossless)'
    L2HC = 'l2hc', 'L2HC'
    LC3 = 'lc3', 'LC3'
    LC3_PLUS = 'lc3_plus', 'LC3+'
    LDAC = 'ldac', 'LDAC'
    LHDC = 'lhdc', 'LHDC'
    SBC = 'sbc', 'SBC'

class ConnectorType(models.TextChoices):
    LIGHTNING = 'lightning', 'Lightning'
    MICROUSB_2_0 = 'microusb_2_0', 'microUSB 2.0'
    MICROUSB_3_0 = 'microusb_3_0', 'microUSB 3.0'
    USB_C = 'usb_c', 'USB Type-C'
    USB_C_2_0 = 'usb_c_2_0', 'USB Type-C 2.0'
    USB_C_3_2_GEN1 = 'usb_c_3_2_gen1', 'USB Type-C 3.2 Gen1'
    USB_C_3_2_GEN1_PLUS_2_0 = 'usb_c_3_2_gen1_plus_2_0', 'USB Type-C 3.2 Gen1 + USB Type-C 2.0'
    USB_C_3_2_GEN2 = 'usb_c_3_2_gen2', 'USB Type-C 3.2 Gen2'

class BatteryType(models.TextChoices):
    LI_ION = 'li_ion', 'Li-ion'
    LI_POL = 'li_pol', 'Li-pol'
    SI_C = 'si_c', 'Si-C'

class BatteryDesign(models.TextChoices):
    REMOVABLE = 'removable', 'Съёмный'
    NON_REMOVABLE = 'non_removable', 'Несъёмный'


































