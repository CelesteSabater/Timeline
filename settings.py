win_condition = 10
fails = 0
lose_condition = 3

mesa = {}

mazo_inventos = {'Agujas de hueso Pinceles':'-20000',
'Cabañas de hueso de mamut':'-18000',
'Arpones':'-13000',
'Cestería en mimbre Vasijas de arcilla':'-12000',
'Redes de pesca Peine ':'-10000',
'Canoas':'-10000',
'Fundición de cobre':'-8000',
'Rueda Balanza':'-7500',
'Ladrillo':'-6500',
'Embarcaciones de vela':'-3500',
'Arado ':'-3500',
'Escritura Cuneiforme':'-3300',
'Calendario':'-3300',
'La palanca':'-1500',
'El tornillo sin fin':'-1500',
'El tornillo elevador de agua':'-1500',
'La balanza hidrostática':'-1500',
'Los espejos ustorios':'-1500',
'Sismoscopio':'-1500',
'Herradura':'50',
'Papel ':'105',
'Cúpula':'124',
'Carro con ruedas':'200',
'Estribos':'350',
'Astrolabio ':'400',
'Molino de Viento ':'650',
'Papel Moneda':'800',
'Pólvora':'800',
'Impresión de libros ':'868',
'Arado de ruedas':'950',
'Cristales coloreados en ventanas de Inglaterra':'999',
'Partituras':'1000',
'Lentes':'1000',
'Cámara oscura':'1000',
'Brújula magnética ':'1100',
'Primer molino de viento en Francia':'1105',
'Cañón (Usado por los moros)':'1118',
'Clavecín':'1121',
'Timón de popa':'1200',
'Globos de aire caliente (China)':'1232',
'Espejos cóncavos':'1257',
'Anteojos':'1268',
'Máquina de bobinas de seda':'1272',
'Bolonia':'1280',
'Reloj mecánico ':'1298',
'Rueda de hilar':'1400',
'Pinturas al óleo':'1420',
'Velocípedo':'1450',
'Imprenta de tipos móviles Laúd':'1500',
'Reloj':'1500',
'Puntilla':'1500',
'Lápiz':'1565',
'Péndulo':'1581',
'Mapa en proyección':'1569',
'Telar':'1589',
'Inodoro':'1589',
'Microscopio compuesto':'1590',
'Termómetro de agua':'1593',
'Telescopio refractor':'1609',
'Diligencia':'1620',
'Submarino':'1620',
'Bayoneta':'1640',
'Calculadora de Pascal':'1642',
'Reloj de péndulo':'1657',
'Microscopio mejorado':'1665',
'Telescopio reflector':'1668',
'Bomba neumática':'1672',
'Higrómetro':'1687',
'Piano ':'1709',
'Termómetro de alcohol':'1710',
'Máquina de vapor Newcomen':'1712',
'Termómetro de mercurio':'1714',
'Octante':'1731',
'Lanzadera automática':'1733',
'Estufa Franklin':'1740',
'Imprenta en colores':'1740',
'Escala centígrada':'1742',
'Condensador eléctrico':'1745',
'Pararrayos':'1752',
'Sextante':'1757',
'Cronómetro':'1761',
'Reflectores parabólicos':'1763',
'Automóvil de vapor':'1769',
'Volante':'1776',
'Máquina de vapor Watt':'1782',
'Globo de aire caliente':'1783',
'Lámpara de aceite, con mecha hueca':'1784',
'Electróforo':'1785',
'Hélice':'1790',
'Sistema métrico':'1795',
'Vacuna':'1796',
'Litografías':'1796',
'Martillo Pilón':'1800',
'Pila eléctrica':'1801',
'Electróforo':'1801',
'Endiómetro':'1801',
'Locomotora de Vapor':'1802',
'Acumulador eléctrico':'1803',
'Telar Jacquard':'1805',
'Lámpara de seguridad para mineros':'1816',
'Termoelectricidad':'1816',
'Fósforos':'1821',
'Cortadora de césped':'1827',
'Dínamo eléctrica':'1830',
'Cosechadora':'1831',
'Telégrafo eléctrico':'1834',
'Alfabeto Morse':'1837',
'Estereoscopio':'1837',
'Bicicleta':'1838',
'Estampilla de Correos':'1839',
'Buques con casco de hierro':'1840',
'Reloj eléctrico':'1840',
'Anestésicos':'1842',
'Saxofón':'1846',
'Prensa rotativa':'1846',
'Cerradura de seguridad':'1846',
'Cámara de placas':'1851',
'Linóleo':'1860',
'Esquiladora':'1860',
'Máquina de escribir':'1870',
'Frigorífico':'1876',
'Fonógrafo':'1877',
'Motor de cuatro tiempos':'1877',
'Bombita eléctrica':'1880',
'Generador de turbina de vapor':'1884',
'Automóvil':'1885',
'Bicicleta de pedales':'1885',
'Gramófono':'1888',
'Ascensor eléctrico':'1889',
'Rayos X':'1890',
'El tubo de Crookes':'1890',
'Radio':'1894',
'Primer periscopio':'1894',
'Motor Diesel':'1897',
'Motor eléctrico compacto':'1897',
'El dirigible rígido Zeppelin':'1900',
'Tractor':'1900',
'Mecano':'1901',
'Frenos de disco ':'1902',
'Cuchilla de seguridad':'1903',
'Máquina de hacer botellas':'1903',
'Electrocardiograma':'1903',
'Cinturón de Seguridad':'1903',
'Osito de peluche':'1903',
'Lámpara Termoiónica':'1906',
'Lavarropas':'1907',
'Fundación de la Sociedad de Inventores Argentinos':'1910',
'Modelo nuclear del átomo':'1910',
'Cadena de montaje':'1911',
'Heladera Eléctrica':'1913',
'Cremallera':'1913',
'Semáforos Luminosos':'1913',
'Limpiaparabrisas':'1914',
'Secador de Pelo':'1920',
'Contador Geiger':'1922',
'Televisor':'1925',
'Caucho sintético':'1926',
'Antibióticos':'1927',
'Ciclotrón':'1927',
'Motor a Reacción':'1930',
'Microscopio Electrónico':'1931',
'Guitarra Eléctrica':'1932',
'Grabaciones Estéreo Polietileno':'1933',
'Nylon':'1934',
'Radar':'1935',
'Café Instantáneo':'1938',
'Fotocopiadora':'1938',
'Bolígrafo':'1938',
'Aerosoles':'1941',
'Reactor Nuclear':'1942',
'Equipo de Inmersión':'1942',
'Turbina de reacción para aviones':'1943',
'Calculadora electrónica':'1946',
'Computadora':'1946',
'Transistor':'1946',
'Long Play - Disco de Larga Duración':'1947',
'Neumáticos Radiales':'1948',
'Tarjeta de Crédito':'1950',
'Central Nuclear':'1954',
'Radio a transistores':'1954',
'Plancha de vapor':'1955',
'Velcro':'1956',
'Video Cámara':'1956',
'Satélite Espacial':'1957',
'Aerodeslizador':'1958',
'Chip de Silicio':'1959',
'Lycra':'1959',
'Teflón':'1960',
'Robot Industrial':'1962',
'Satélite de Comunicaciones':'1962',
'Video Casettera':'1963',
'Procesador de Textos':'1964',
'Avión Jumbo':'1969',
'Reloj Digital':'1971',
'Video juegos domésticos':'1972',
'Protocolo de Internet (IP) y Protocolo de Control de Transmisión (TCP)':'1972',
'Códigos de Barras Computadora Personal Walkman':'1973',
'Catalizadores para automotores':'1974',
'Cubo de Rubik':'1980',
'Transbordador Espacial':'1981',
'Papeles autoadhesivos':'1981',
'Tarjeta inteligente':'1982',
'Corazón Artificial':'1982',
'Discos Compactos':'1982',
'Realidad Virtual':'1990',
'Fusión Nuclear':'1990',
'Identificador de voz':'1990',
'Videófono':'1991'
}