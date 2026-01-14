from django.db import models
from django.conf import settings

from .choices import (
    PhoneType,
    OperationSystem,
    ScreenTechnology,
    RefreshRate,
    RamSize,
    StorageSize,
    VideoResolution,
    MemoryCard,
    OSVersion,
    CameraMegapixels,
    SimSlots,
    SimType,
    Platform,
    CpuCores,
    ProcessTechnology,
    BodyConstruction,
    FrameMaterial,
    BackCoverMaterial,
    BackCoverColor,
    OpticalZoom,
    MainCameraAperture,
    BluetoothAudioCodecs,
    ConnectorType,
    BatteryType,
    BatteryDesign,
)


class Mobile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mobiles')

    title = models.CharField(max_length=500, verbose_name='Название модели')
    image = models.ImageField(upload_to='mobiles_images/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    type = models.CharField(max_length=20, choices=PhoneType.choices, blank=True, null=True,
                            verbose_name='Тип телефона')
    operating_system = models.CharField(max_length=30, choices=OperationSystem.choices, blank=True, null=True,
                                        verbose_name='Операционная система')

    os_version_at_release = models.CharField(max_length=30, choices=OSVersion.choices, blank=True, null=True,
                                             verbose_name='Версия ОС на момент выхода')

    screen_size = models.CharField(max_length=20, blank=True, null=True, verbose_name='Размер экрана (дюймов)')
    screen_resolution = models.CharField(max_length=30, blank=True, null=True, verbose_name='Разрешение экрана')
    screen_technology = models.CharField(max_length=20, choices=ScreenTechnology.choices, blank=True, null=True,
                                         verbose_name='Технология экрана')
    refresh_rate = models.CharField(max_length=20, choices=RefreshRate.choices, blank=True, null=True,
                                    verbose_name='Частота обновления экрана', help_text='Гц')
    ram_size = models.CharField(max_length=20, choices=RamSize.choices, blank=True, null=True,
                                verbose_name='Оперативная память')
    storage_size = models.CharField(max_length=20, choices=StorageSize.choices, blank=True, null=True,
                                    verbose_name='Встроенная память')

    main_camera_megapixels = models.CharField(max_length=10, choices=CameraMegapixels.choices, blank=True, null=True,
                                              verbose_name='Основная камера (Мп)')

    camera_specs = models.TextField(blank=True, null=True, verbose_name='Характеристики камеры')
    max_video_resolution = models.CharField(max_length=30, choices=VideoResolution.choices, blank=True, null=True,
                                            verbose_name='Максимальное разрешение видео')
    fast_charging = models.BooleanField(default=False, verbose_name='Быстрая зарядка')

    memory_card_support = models.BooleanField(default=False, verbose_name='Поддержка карты памяти')

    sim_slots = models.CharField(max_length=1, blank=True, null=True, verbose_name='Количество SIM-карт')

    sim_type = models.CharField(max_length=10, choices=SimType.choices, blank=True, null=True,
                                verbose_name='Тип SIM-карты')

    platform = models.CharField(max_length=50, choices=Platform.choices, blank=True, null=True,
                                verbose_name='Платформа')

    cpu_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модель процессора')

    cpu_cores = models.CharField(max_length=25, choices=CpuCores.choices, blank=True, null=True,
                                 verbose_name='Количество ядер процессора')

    cpu_architecture = models.CharField(max_length=50, blank=True, null=True, verbose_name='Архитектура процессора')

    process_technology = models.CharField(max_length=5, choices=ProcessTechnology.choices, blank=True, null=True,
                                          verbose_name='Техпроцесс')

    gpu_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Графический процессор')
    modem = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модем')

    body_construction = models.CharField(max_length=40, choices=BodyConstruction.choices, blank=True, null=True,
                                         verbose_name='Конструкция корпуса')

    stereo_speakers = models.BooleanField(default=False, verbose_name='Стереодинамики')

    frame_material = models.CharField(max_length=40, choices=FrameMaterial.choices, blank=True, null=True,
                                      verbose_name='Материал рамки')

    back_cover_material = models.CharField(max_length=20, choices=BackCoverMaterial.choices, blank=True, null=True,
                                           verbose_name='Материал задней крышки')

    frame_color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Цвет рамки')
    back_cover_color = models.CharField(max_length=40, choices=BackCoverColor.choices, blank=True, null=True,
                                        verbose_name='Цвет задней крышки')

    front_panel_color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Цвет фронтальной панели')
    shockproof = models.BooleanField(default=False, verbose_name='Ударопрочность')

    water_dust_protection = models.BooleanField(default=False, verbose_name='Защита от воды и пыли')
    built_in_magnets = models.BooleanField(default=False, verbose_name='Встроенные магниты')
    physical_keyboard = models.BooleanField(default=False, verbose_name='Физическая клавиатура')
    fingerprint_scanner = models.BooleanField(default=False, verbose_name='Сканер отпечатка пальца')
    face_unlock = models.BooleanField(default=False, verbose_name='Разблокировка по лицу')

    special_features = models.TextField(blank=True, null=True, verbose_name='Особенности')

    length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Длина (мм)')
    width = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Ширина (мм)')
    thickness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Толщина (мм)')
    weight = models.PositiveIntegerField(blank=True, null=True, verbose_name='Вес (г)')

    screen_colors = models.CharField(max_length=50, blank=True, null=True,
                                     verbose_name='Количество отображаемых цветов')
    screen_ppi = models.PositiveIntegerField(blank=True, null=True, verbose_name='Плотность пикселей (PPI)')
    aspect_ratio = models.CharField(max_length=20, blank=True, null=True, verbose_name='Соотношение сторон')

    brightness_typical = models.PositiveIntegerField(blank=True, null=True, verbose_name='Типичная яркость (кд/м²)')
    brightness_peak = models.PositiveIntegerField(blank=True, null=True, verbose_name='Пиковая яркость (кд/м²)')

    touchscreen = models.BooleanField(default=True, verbose_name='Сенсорный экран')

    scratch_protection = models.BooleanField(default=False, verbose_name='Защита от царапин')

    always_on_display = models.BooleanField(default=False, verbose_name='Always-On Display')
    ltpo_support = models.BooleanField(default=False, verbose_name='Поддержка LTPO')

    main_camera = models.CharField(max_length=50, blank=True, null=True, verbose_name='Основная камера')
    camera_modules_count = models.PositiveSmallIntegerField(blank=True, null=True,
                                                            verbose_name='Количество модулей камеры')
    camera_modules = models.TextField(blank=True, null=True, verbose_name='Модули камеры')

    flash = models.BooleanField(default=False, verbose_name='Вспышка')
    autofocus = models.BooleanField(default=False, verbose_name='Автофокус')
    optical_stabilization = models.BooleanField(default=False, verbose_name='Оптическая стабилизация')

    optical_zoom = models.CharField(max_length=30, choices=OpticalZoom.choices, blank=True, null=True,
                                    verbose_name='Оптический зум')

    main_camera_aperture = models.CharField(max_length=20, choices=MainCameraAperture.choices, blank=True, null=True,
                                            verbose_name='Диафрагма основной камеры')

    max_fps = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Максимальный FPS видео')

    front_camera = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фронтальная камера')
    front_camera_specs = models.TextField(blank=True, null=True, verbose_name='Характеристики фронтальной камеры')
    front_camera_position = models.CharField(max_length=50, blank=True, null=True,
                                             verbose_name='Расположение фронтальной камеры')

    dual_front_camera = models.BooleanField(default=False, verbose_name='Двойная фронтальная камера')
    front_autofocus = models.BooleanField(default=False, verbose_name='Автофокус фронтальной камеры')
    front_flash = models.BooleanField(default=False, verbose_name='Вспышка фронтальной камеры')
    front_camera_aperture = models.CharField(max_length=20, blank=True, null=True,
                                             verbose_name='Диафрагма фронтальной камеры')
    front_max_video_resolution = models.CharField(max_length=50, blank=True, null=True,
                                                  verbose_name='Максимальное видео фронтальной камеры')

    accelerometer = models.BooleanField(default=False, verbose_name='Акселерометр')
    gyroscope = models.BooleanField(default=False, verbose_name='Гироскоп')
    light_sensor = models.BooleanField(default=False, verbose_name='Датчик освещённости')
    proximity_sensor = models.BooleanField(default=False, verbose_name='Датчик приближения')
    barometer = models.BooleanField(default=False, verbose_name='Барометр')
    heart_rate_monitor = models.BooleanField(default=False, verbose_name='Датчик пульса')
    spo2_sensor = models.BooleanField(default=False, verbose_name='Датчик SpO₂')

    gps = models.BooleanField(default=False, verbose_name='GPS')
    glonass = models.BooleanField(default=False, verbose_name='ГЛОНАСС')
    beidou = models.BooleanField(default=False, verbose_name='BeiDou')
    galileo = models.BooleanField(default=False, verbose_name='Galileo')

    edge = models.BooleanField(default=False, verbose_name='EDGE')
    hspa = models.BooleanField(default=False, verbose_name='HSPA')
    hspa_plus = models.BooleanField(default=False, verbose_name='HSPA+')
    lte = models.BooleanField(default=False, verbose_name='LTE')
    five_g = models.BooleanField(default=False, verbose_name='5G')

    bluetooth = models.BooleanField(default=False, verbose_name='Bluetooth')

    bluetooth_audio_codecs = models.CharField(max_length=100, choices=BluetoothAudioCodecs.choices, blank=True,
                                              null=True, verbose_name='Аудиокодеки Bluetooth')

    audio_jack = models.BooleanField(default=False, verbose_name='Аудиоразъём 3.5 мм')
    wifi = models.BooleanField(default=False, verbose_name='Wi-Fi')

    connector_type = models.CharField(max_length=50, choices=ConnectorType.choices, blank=True, null=True,
                                      verbose_name='Тип разъёма')

    nfc = models.BooleanField(default=False, verbose_name='NFC')

    battery_type = models.CharField(max_length=50, choices=BatteryType.choices, blank=True, null=True,
                                    verbose_name='Тип аккумулятора')

    battery_capacity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Ёмкость аккумулятора (мА·ч)')

    battery_design = models.CharField(max_length=50, choices=BatteryDesign.choices, blank=True, null=True,
                                      verbose_name='Конструкция аккумулятора')

    max_video_playback_time = models.CharField(max_length=50, blank=True, null=True,
                                               verbose_name='Время воспроизведения видео')

    package_contents = models.TextField(blank=True, null=True, verbose_name='Комплектация')
    case_included = models.BooleanField(default=False, verbose_name='Чехол в комплекте')
    stylus_included = models.BooleanField(default=False, verbose_name='Стилус в комплекте')

    owner_contacts = models.TextField(verbose_name='Контактная информация владельца')

    def __str__(self):
        return self.title
