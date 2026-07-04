// RO/RU localization for the audit API (findings, template summary, errors).
// EN text is produced inline in functions/api/audit.js; this module only adds
// ro/ru, and the caller falls back to EN per item when a key is missing.

export const AUDIT_LANGS = ['en', 'ro', 'ru'];

export function pickLang(raw) {
  return AUDIT_LANGS.indexOf(String(raw || '')) !== -1 ? String(raw) : 'en';
}

// Per-id { title, detail } templates. Placeholders: {count} {vals} {title} {perf} {secs}
const FINDINGS = {
  ro: {
    https: { title: 'Site servit prin HTTP simplu', detail: 'Browserele marchează site-ul „Not secure” lângă numele afacerii tale. Doar asta și vizitatorii pleacă.' },
    tel_missing: { title: 'Numărul de telefon nu poate fi apăsat', detail: 'Pe pagină apare un număr de telefon, dar nu este un link tel:. Pe mobil, unde sunt majoritatea clienților locali, trebuie să îl memoreze și să îl retasteze. Acolo se pierd apelurile.' },
    tel_broken: { title: '{count} linkuri click-to-call defecte', detail: 'Există linkuri tel:, dar țintele lor sunt greșite ({vals}). Apăsarea lor nu face nimic, cel mai costisitor tip de defect tăcut pentru o afacere de servicii.' },
    no_contact_path: { title: 'Nicio cale evidentă de a te contacta', detail: 'Niciun formular, niciun link de email, niciun telefon apăsabil, niciun link către pagina de contact pe această pagină. Un vizitator gata să cumpere trebuie să se chinuie să ajungă la tine, iar majoritatea nu o vor face.' },
    no_schema: { title: 'Niciun fel de date structurate', detail: 'Google și asistenții AI citesc marcajul schema.org ca să înțeleagă cine ești, unde activezi și ce vinzi. Fără el, pentru ei ești doar un perete de text.' },
    no_business_schema: { title: 'Lipsă schema LocalBusiness / Organization', detail: 'Există date structurate, dar nimic nu identifică afacerea în sine: nume, zonă deservită, telefon. Exact blocul pe care îl folosesc căutarea locală și asistenții AI.' },
    self_rating: { title: 'Marcaj de rating cu stele auto-atribuit', detail: 'aggregateRating pe propria entitate de business încalcă ghidul Google pentru date structurate și poate atrage o penalizare manuală. Stelele țin de platformele de recenzii terțe.' },
    no_title: { title: 'Lipsește titlul paginii', detail: 'Eticheta <title> este titlul rezultatului tău în Google. Fără ea, Google improvizează unul în locul tău.' },
    thin_title: { title: 'Titlul paginii este foarte scurt („{title}”)', detail: 'Titlurile scurte și generice irosesc cel mai valoros câmp SEO de pe pagină.' },
    no_meta_desc: { title: 'Lipsește meta description', detail: 'Acesta este textul de vânzare de sub listarea ta din Google. Când lipsește, Google alege o propoziție la întâmplare, rareori cea care vinde.' },
    no_og: { title: 'Lipsesc tag-urile de partajare socială (Open Graph)', detail: 'Când cineva îți partajează site-ul pe WhatsApp, Viber sau Facebook, previzualizarea e goală sau aleatorie. Partajările fără previzualizare primesc mai puține click-uri.' },
    no_viewport: { title: 'Nu e pregătit pentru mobil (lipsește tag-ul viewport)', detail: 'Fără un meta tag viewport, telefoanele afișează layout-ul de desktop micșorat. Majoritatea traficului de afaceri locale e de pe mobil.' },
    no_h1: { title: 'Niciun titlu H1', detail: 'Motoarele de căutare tratează H1 ca declarația de subiect a paginii. Lipsa lui slăbește un semnal ușor de relevanță.' },
    hreflang_single: { title: 'Set hreflang incomplet', detail: 'Este declarată o singură alternativă hreflang. Un set are nevoie de fiecare versiune de limbă plus x-default, altfel nu face nimic.' },
    no_lang: { title: 'Lipsește atributul lang pe <html>', detail: 'Cititoarele de ecran și motoarele de căutare trebuie să ghicească limba paginii.' },
    no_favicon: { title: 'Niciun favicon declarat', detail: 'Iconița din tab e un lucru mic, dar absența ei se citește ca „neterminat” într-o bară de taburi plină de concurenți îngrijiți.' },
    slow_mobile: { title: 'Lent pe mobil', detail: 'Google PageSpeed dă acestei pagini {perf}/100 pe o conexiune mobilă. Vizitatorii de pe telefon pleacă înainte ca paginile lente să se încarce.' },
    mediocre_mobile: { title: 'Viteza pe mobil mai are loc de mai bine', detail: 'Scorul de performanță pe mobil este {perf}/100. Nu e stricat, dar fiecare secundă de încărcare costă conversii.' },
    mediocre_mobile_poor_lcp: { title: 'Viteza pe mobil are nevoie de lucru serios', detail: 'Scorul de performanță pe mobil este {perf}/100, iar conținutul principal este atât de lent încât intră în banda „slabă” a Google. Pe telefoane asta te costă activ vizitatori, nu e doar șlefuială.' },
    lcp: { title: 'Conținutul principal apare în {secs}s (LCP)', detail: 'Largest Contentful Paint peste 4 secunde este în banda „slabă” a Google, afectează atât pozițiile, cât și răbdarea.' },
    img_alt: { title: '{missing} din {total} imagini nu au text alt', detail: 'Cititoarele de ecran și Google Images se bazează pe textul alt ca să știe ce arată o imagine. {missing} din cele {total} imagini de pe pagină nu au deloc, invizibile pentru tehnologiile asistive și pentru căutarea de imagini.' },
    mixed_content: { title: '{count} resurse nesigure pe o pagină securizată', detail: 'Pagina se încarcă prin HTTPS, dar aduce {count} resurse prin http:// simplu. Browserele le blochează sau avertizează, ceea ce poate strica imagini sau scripturi și scoate lacătul care inspiră încredere.' },
    no_robots: { title: 'Nu există robots.txt', detail: 'Nu există /robots.txt. Motoarele de căutare tot te vor accesa, dar nu ai cum să le ghidezi sau să le arăți sitemap-ul, iar absența lui semnalează adesea un site negestionat.' },
    no_sitemap: { title: 'Nu există sitemap XML', detail: 'Nu există /sitemap.xml și nicio linie Sitemap: în robots.txt. Un sitemap este modul prin care Google descoperă sigur fiecare pagină; fără el, paginile mai adânci pot rămâne neindexate săptămâni întregi.' },
    redirect_chain: { title: '{count} redirecționări până la pagina reală', detail: 'Adresa introdusă trece prin {count} redirecționări înainte să ajungă la pagina finală. Fiecare pas adaugă întârziere pe mobil și pierde puțin din valoarea SEO; lanțurile lungi se strică și mai ușor.' }
  },
  ru: {
    https: { title: 'Сайт отдаётся по простому HTTP', detail: 'Браузеры помечают сайт «Не защищено» рядом с названием вашего бизнеса. Уже одного этого достаточно, чтобы отпугнуть посетителей.' },
    tel_missing: { title: 'Номер телефона нельзя нажать', detail: 'На странице есть номер телефона, но это не ссылка tel:. На мобильном, где большинство локальных клиентов, его приходится запоминать и перенабирать. Именно там теряются звонки.' },
    tel_broken: { title: 'Битых ссылок click-to-call: {count}', detail: 'Ссылки tel: есть, но их адреса некорректны ({vals}). Нажатие на них ничего не делает, самый дорогой вид незаметного дефекта для сервисного бизнеса.' },
    no_contact_path: { title: 'Нет очевидного способа с вами связаться', detail: 'На странице не найдено ни формы, ни email-ссылки, ни нажимаемого телефона, ни ссылки на страницу контактов. Готовому купить посетителю приходится прилагать усилия, и большинство не станет.' },
    no_schema: { title: 'Структурированных данных нет вообще', detail: 'Google и AI-ассистенты читают разметку schema.org, чтобы понять, кто вы, где работаете и что продаёте. Без неё для них вы просто стена текста.' },
    no_business_schema: { title: 'Нет схемы LocalBusiness / Organization', detail: 'Структурированные данные есть, но ничто не описывает сам бизнес: название, зону обслуживания, телефон. Это именно тот блок, который используют локальный поиск и AI-ассистенты.' },
    self_rating: { title: 'Самовыставленная разметка рейтинга со звёздами', detail: 'aggregateRating на вашей собственной бизнес-сущности нарушает рекомендации Google по структурированным данным и может привести к ручным санкциям. Звёзды должны быть на сторонних площадках отзывов.' },
    no_title: { title: 'Отсутствует title страницы', detail: 'Тег <title> это заголовок вашего результата в Google. Без него Google придумывает его за вас.' },
    thin_title: { title: 'Title страницы очень короткий («{title}»)', detail: 'Короткие шаблонные заголовки впустую тратят самое ценное SEO-поле на странице.' },
    no_meta_desc: { title: 'Отсутствует meta description', detail: 'Это продающий текст под вашим объявлением в Google. Когда его нет, Google берёт случайное предложение, редко то, которое продаёт.' },
    no_og: { title: 'Нет тегов для шаринга (Open Graph)', detail: 'Когда кто-то делится вашим сайтом в WhatsApp, Viber или Facebook, превью пустое или случайное. Репосты без превью получают меньше кликов.' },
    no_viewport: { title: 'Не готов к мобильным (нет тега viewport)', detail: 'Без meta-тега viewport телефоны показывают десктопный макет уменьшенным. Большая часть трафика локального бизнеса с мобильных.' },
    no_h1: { title: 'Нет заголовка H1', detail: 'Поисковики воспринимают H1 как формулировку темы страницы. Его отсутствие ослабляет простой сигнал релевантности.' },
    hreflang_single: { title: 'Неполный набор hreflang', detail: 'Объявлена только одна альтернатива hreflang. Набору нужны все языковые версии плюс x-default, иначе он не работает.' },
    no_lang: { title: 'Нет атрибута lang у <html>', detail: 'Скринридерам и поисковикам приходится угадывать язык страницы.' },
    no_favicon: { title: 'Не объявлен favicon', detail: 'Иконка вкладки мелочь, но её отсутствие читается как «недоделано» в ряду вкладок с опрятными конкурентами.' },
    slow_mobile: { title: 'Медленно на мобильном', detail: 'Google PageSpeed даёт этой странице {perf}/100 на мобильном соединении. Посетители с телефонов уходят раньше, чем медленные страницы догрузятся.' },
    mediocre_mobile: { title: 'Скорость на мобильном можно улучшить', detail: 'Оценка производительности на мобильном {perf}/100. Не сломано, но каждая секунда загрузки стоит конверсий.' },
    mediocre_mobile_poor_lcp: { title: 'Скорость на мобильном требует серьёзной работы', detail: 'Оценка производительности на мобильном {perf}/100, а основной контент настолько медленный, что попадает в «плохую» зону Google. На телефонах это активно стоит вам посетителей, а не просто полировки.' },
    lcp: { title: 'Основной контент появляется за {secs}с (LCP)', detail: 'Largest Contentful Paint выше 4 секунд в «плохой» зоне Google, это бьёт и по позициям, и по терпению.' },
    img_alt: { title: '{missing} из {total} изображений без alt-текста', detail: 'Скринридеры и Google Картинки опираются на alt-текст, чтобы понять, что на изображении. У {missing} из {total} изображений на странице его нет, они невидимы для вспомогательных технологий и для поиска по картинкам.' },
    mixed_content: { title: '{count} небезопасных ресурсов на защищённой странице', detail: 'Страница загружается по HTTPS, но подтягивает {count} ресурсов по простому http://. Браузеры блокируют их или предупреждают, из-за чего могут ломаться картинки или скрипты, и пропадает замок, вызывающий доверие.' },
    no_robots: { title: 'Файл robots.txt не найден', detail: 'Нет /robots.txt. Поисковики всё равно будут вас сканировать, но вы никак не управляете ими и не указываете им карту сайта, а его отсутствие часто говорит о заброшенном сайте.' },
    no_sitemap: { title: 'XML-карта сайта не найдена', detail: 'Нет /sitemap.xml и нет строки Sitemap: в robots.txt. Карта сайта это то, как Google надёжно находит каждую страницу; без неё глубокие страницы могут неделями оставаться неиндексированными.' },
    redirect_chain: { title: '{count} редиректов до настоящей страницы', detail: 'Введённый адрес проходит через {count} редиректов, прежде чем попасть на конечную страницу. Каждый переход добавляет задержку на мобильном и теряет немного SEO-веса; длинные цепочки чаще ломаются.' }
  }
};

// Per-id one-line fix instruction. EN is the source; ro/ru fall back to en.
const FIX = {
  en: {
    https: 'Install a free SSL certificate (most hosts do it in one click) and force https://.',
    tel_missing: 'Wrap the number in a tel: link, e.g. <a href="tel:+373...">.',
    tel_broken: 'Fix the tel: targets to digits only with the country code (tel:+373...).',
    no_contact_path: 'Add a contact form or a tappable phone/email high on the page.',
    no_schema: 'Add LocalBusiness JSON-LD with name, address, phone and opening hours.',
    no_business_schema: 'Add a LocalBusiness or Organization block to your existing schema.',
    self_rating: 'Remove aggregateRating from your own entity; keep reviews on third-party platforms.',
    no_title: 'Add a <title> with your business + main service + city.',
    thin_title: 'Expand the title to business + main service + city (50-60 characters).',
    no_meta_desc: 'Write a ~150-character meta description that sells the click.',
    no_og: 'Add og:title, og:description and og:image so shared links show a preview.',
    no_viewport: 'Add <meta name="viewport" content="width=device-width, initial-scale=1">.',
    no_h1: 'Add a single H1 that states what the page is about.',
    hreflang_single: 'Declare every language version plus an x-default, or remove the lone tag.',
    no_lang: 'Set <html lang="..."> to the page language.',
    no_favicon: 'Add a favicon (<link rel="icon">) — most builders have a one-click upload.',
    slow_mobile: 'Compress images, defer non-critical scripts, enable caching/CDN.',
    mediocre_mobile: 'Trim image weight and unused scripts to claw back the easy seconds.',
    mediocre_mobile_poor_lcp: 'Fix the largest image/banner first (compress, right-size, preload), then defer non-critical scripts.',
    lcp: 'Optimize the largest image/banner: compress it, size it right, preload it.',
    img_alt: 'Add descriptive alt text to every content image; use alt="" only for purely decorative ones.',
    mixed_content: 'Switch the http:// asset links to https:// (or protocol-relative //) so nothing loads insecurely.',
    no_robots: 'Add a /robots.txt (even a permissive one) and point it at your sitemap.',
    no_sitemap: 'Publish an XML sitemap and reference it in robots.txt so search engines find every page.',
    redirect_chain: 'Link and reference the final https:// URL directly to cut the extra redirect hops.'
  },
  ro: {
    https: 'Instalează un certificat SSL gratuit (majoritatea hostingurilor o fac dintr-un clic) și forțează https://.',
    tel_missing: 'Pune numărul într-un link tel:, ex. <a href="tel:+373...">.',
    tel_broken: 'Corectează țintele tel: la doar cifre cu prefixul de țară (tel:+373...).',
    no_contact_path: 'Adaugă un formular de contact sau un telefon/email apăsabil sus pe pagină.',
    no_schema: 'Adaugă JSON-LD LocalBusiness cu nume, adresă, telefon și program.',
    no_business_schema: 'Adaugă un bloc LocalBusiness sau Organization la schema existentă.',
    self_rating: 'Scoate aggregateRating de pe propria entitate; ține recenziile pe platforme terțe.',
    no_title: 'Adaugă un <title> cu afacerea + serviciul principal + orașul.',
    thin_title: 'Extinde titlul la afacere + serviciu principal + oraș (50-60 caractere).',
    no_meta_desc: 'Scrie o meta description de ~150 de caractere care vinde click-ul.',
    no_og: 'Adaugă og:title, og:description și og:image ca linkurile partajate să arate o previzualizare.',
    no_viewport: 'Adaugă <meta name="viewport" content="width=device-width, initial-scale=1">.',
    no_h1: 'Adaugă un singur H1 care spune despre ce e pagina.',
    hreflang_single: 'Declară fiecare versiune de limbă plus un x-default, sau scoate tag-ul singular.',
    no_lang: 'Setează <html lang="..."> la limba paginii.',
    no_favicon: 'Adaugă un favicon (<link rel="icon">) — majoritatea platformelor au upload dintr-un clic.',
    slow_mobile: 'Comprimă imaginile, amână scripturile necritice, activează caching/CDN.',
    mediocre_mobile: 'Reduce greutatea imaginilor și scripturile nefolosite ca să recuperezi secundele ușoare.',
    mediocre_mobile_poor_lcp: 'Repară întâi imaginea/bannerul cel mai mare (comprimă, dimensionează corect, preload), apoi amână scripturile necritice.',
    lcp: 'Optimizează imaginea/bannerul cel mai mare: comprimă, dimensionează corect, fă-i preload.',
    img_alt: 'Adaugă text alt descriptiv la fiecare imagine de conținut; folosește alt="" doar pentru cele pur decorative.',
    mixed_content: 'Schimbă linkurile de resurse http:// în https:// (sau protocol-relative //) ca nimic să nu se încarce nesigur.',
    no_robots: 'Adaugă un /robots.txt (chiar și permisiv) și indică-i sitemap-ul.',
    no_sitemap: 'Publică un sitemap XML și referă-l în robots.txt ca motoarele de căutare să găsească fiecare pagină.',
    redirect_chain: 'Leagă și referă direct URL-ul final https:// ca să elimini pașii de redirecționare în plus.'
  },
  ru: {
    https: 'Установите бесплатный SSL-сертификат (у большинства хостингов это в один клик) и принудительно включите https://.',
    tel_missing: 'Оберните номер в ссылку tel:, напр. <a href="tel:+373...">.',
    tel_broken: 'Исправьте адреса tel: на только цифры с кодом страны (tel:+373...).',
    no_contact_path: 'Добавьте форму контакта или кликабельный телефон/email вверху страницы.',
    no_schema: 'Добавьте JSON-LD LocalBusiness с названием, адресом, телефоном и часами работы.',
    no_business_schema: 'Добавьте блок LocalBusiness или Organization к существующей схеме.',
    self_rating: 'Уберите aggregateRating со своей сущности; отзывы держите на сторонних площадках.',
    no_title: 'Добавьте <title> с бизнесом + основной услугой + городом.',
    thin_title: 'Расширьте title до бизнес + основная услуга + город (50-60 символов).',
    no_meta_desc: 'Напишите meta description ~150 символов, продающую клик.',
    no_og: 'Добавьте og:title, og:description и og:image, чтобы у ссылок было превью.',
    no_viewport: 'Добавьте <meta name="viewport" content="width=device-width, initial-scale=1">.',
    no_h1: 'Добавьте один H1, который говорит, о чём страница.',
    hreflang_single: 'Объявите все языковые версии плюс x-default или уберите одиночный тег.',
    no_lang: 'Задайте <html lang="..."> языку страницы.',
    no_favicon: 'Добавьте favicon (<link rel="icon">) — у большинства конструкторов загрузка в один клик.',
    slow_mobile: 'Сожмите изображения, отложите некритичные скрипты, включите кеширование/CDN.',
    mediocre_mobile: 'Уменьшите вес картинок и неиспользуемые скрипты, чтобы вернуть лёгкие секунды.',
    mediocre_mobile_poor_lcp: 'Сначала займитесь самым большим изображением/баннером (сжатие, правильный размер, preload), затем отложите некритичные скрипты.',
    lcp: 'Оптимизируйте самое большое изображение/баннер: сжатие, правильный размер, preload.',
    img_alt: 'Добавьте описательный alt-текст к каждому смысловому изображению; alt="" оставьте только для чисто декоративных.',
    mixed_content: 'Замените http:// ссылки на ресурсы на https:// (или протокол-относительные //), чтобы ничего не грузилось небезопасно.',
    no_robots: 'Добавьте /robots.txt (пусть даже разрешающий) и укажите в нём карту сайта.',
    no_sitemap: 'Опубликуйте XML-карту сайта и сошлитесь на неё в robots.txt, чтобы поисковики находили каждую страницу.',
    redirect_chain: 'Ссылайтесь сразу на конечный https:// URL, чтобы убрать лишние переходы-редиректы.'
  }
};

// Rough effort per id (a code token) and its localized label.
const EFFORT = {
  https: '30m', tel_missing: '15m', tel_broken: '15m', no_contact_path: '1h', no_schema: '1h',
  no_business_schema: '30m', self_rating: '15m', no_title: '10m', thin_title: '10m', no_meta_desc: '15m',
  no_og: '20m', no_viewport: '5m', no_h1: '10m', hreflang_single: '30m', no_lang: '5m', no_favicon: '10m',
  slow_mobile: 'halfday', mediocre_mobile: '2h', mediocre_mobile_poor_lcp: '2h', lcp: '2h',
  img_alt: '30m', mixed_content: '30m', no_robots: '10m', no_sitemap: '30m', redirect_chain: '30m'
};
const EFFORT_LABEL = {
  en: { '5m': '5 min', '10m': '10 min', '15m': '15 min', '20m': '20 min', '30m': '30 min', '1h': '1 hour', '2h': '2 hours', halfday: 'half a day' },
  ro: { '5m': '5 min', '10m': '10 min', '15m': '15 min', '20m': '20 min', '30m': '30 min', '1h': '1 oră', '2h': '2 ore', halfday: 'o jumătate de zi' },
  ru: { '5m': '5 мин', '10m': '10 мин', '15m': '15 мин', '20m': '20 мин', '30m': '30 мин', '1h': '1 час', '2h': '2 часа', halfday: 'полдня' }
};

// "What's already right" — labels for checks that passed.
const PASSED = {
  en: {
    https: 'Secure HTTPS connection', tappable_phone: 'Tappable phone number', contact: 'Clear way to get in touch',
    schema: 'Structured data present', business_schema: 'Business identity in schema', title: 'Page title set',
    meta_desc: 'Meta description present', og: 'Social share preview tags', viewport: 'Mobile-ready viewport',
    h1: 'Clear H1 heading', lang: 'Page language declared', favicon: 'Favicon present', fast_mobile: 'Fast on mobile',
    img_alt: 'Images have alt text', no_mixed_content: 'No insecure (mixed) content', robots: 'robots.txt present', sitemap: 'XML sitemap present'
  },
  ro: {
    https: 'Conexiune HTTPS securizată', tappable_phone: 'Număr de telefon apăsabil', contact: 'Cale clară de contact',
    schema: 'Date structurate prezente', business_schema: 'Identitatea afacerii în schema', title: 'Titlu de pagină setat',
    meta_desc: 'Meta description prezentă', og: 'Tag-uri de previzualizare la partajare', viewport: 'Viewport pregătit pentru mobil',
    h1: 'Titlu H1 clar', lang: 'Limba paginii declarată', favicon: 'Favicon prezent', fast_mobile: 'Rapid pe mobil',
    img_alt: 'Imaginile au text alt', no_mixed_content: 'Fără conținut nesigur (mixt)', robots: 'robots.txt prezent', sitemap: 'Sitemap XML prezent'
  },
  ru: {
    https: 'Защищённое HTTPS-соединение', tappable_phone: 'Кликабельный номер телефона', contact: 'Понятный способ связаться',
    schema: 'Структурированные данные есть', business_schema: 'Идентификация бизнеса в схеме', title: 'Заголовок страницы задан',
    meta_desc: 'Meta description присутствует', og: 'Теги превью для шаринга', viewport: 'Viewport готов к мобильным',
    h1: 'Чёткий заголовок H1', lang: 'Язык страницы указан', favicon: 'Favicon присутствует', fast_mobile: 'Быстро на мобильном',
    img_alt: 'У изображений есть alt-текст', no_mixed_content: 'Нет небезопасного (смешанного) контента', robots: 'robots.txt присутствует', sitemap: 'XML-карта сайта присутствует'
  }
};

function interp(s, vars) {
  if (!vars) return s;
  return s.replace(/\{(\w+)\}/g, (m, k) => (k in vars && vars[k] != null ? String(vars[k]) : m));
}

export function localizeFindings(findings, lang) {
  const dict = FINDINGS[lang] || null; // null for en — title/detail come from the API inline
  const fixDict = FIX[lang] || FIX.en;
  const effLabel = EFFORT_LABEL[lang] || EFFORT_LABEL.en;
  return (findings || []).map((x) => {
    const t = dict && dict[x.id];
    const out = {
      id: x.id,
      severity: x.severity,
      title: t ? interp(t.title, x.vars) : x.title,
      detail: t ? interp(t.detail, x.vars) : x.detail,
      vars: x.vars,
    };
    const fix = fixDict[x.id] || FIX.en[x.id];
    if (fix) out.fix = interp(fix, x.vars);
    const tok = EFFORT[x.id];
    if (tok) out.effort = effLabel[tok] || EFFORT_LABEL.en[tok];
    return out;
  });
}

// "What's already right" — map passed check ids to localized labels.
export function localizePassed(passed, lang) {
  const dict = PASSED[lang] || PASSED.en;
  return (passed || []).map((id) => ({ id, label: dict[id] || PASSED.en[id] || id }));
}

// Localized template summary (fallback when the LLM summary is not used).
export function localizedSummary(findings, lang) {
  const highs = findings.filter((x) => x.severity === 'high').length;
  const n = findings.length;
  const rest = n - highs;
  if (lang === 'ro') {
    if (n === 0) return 'Trecut curat: niciunul dintre defectele obișnuite ale căii de conversie nu a apărut pe această pagină. Câștigurile rămase țin de copy, ofertă și optimizarea vitezei, nu de instalații sparte.';
    if (highs > 0) return highs + (highs === 1 ? ' problemă care îți pierde activ clienți' : ' probleme care îți pierd activ clienți') + ', plus încă ' + rest + ' mai mici. Elementele de severitate mare sunt exact cele pe care un vizitator le lovește, eșuează în tăcere și nu îți spune niciodată.';
    return 'Niciun ucigaș de conversie, dar ' + n + (n === 1 ? ' îmbunătățire ar strânge' : ' îmbunătățiri ar strânge') + ' felul în care motoarele de căutare și vizitatorii citesc site-ul.';
  }
  if (lang === 'ru') {
    if (n === 0) return 'Чистый проход: ни один из обычных дефектов пути к конверсии на этой странице не обнаружен. Оставшиеся выигрыши в тексте, предложении и тонкой настройке скорости, а не в сломанной механике.';
    if (highs > 0) return 'Найдено серьёзных проблем: ' + highs + ', которые активно теряют вам заявки, плюс ещё ' + rest + ' помельче. Проблемы высокой серьёзности это как раз то, на чём посетитель спотыкается, молча уходит и никогда вам не сообщает.';
    return 'Убийц конверсии нет, но есть ' + n + ' момент(ов) для улучшения того, как поисковики и посетители читают сайт.';
  }
  return null; // en handled by the caller
}

const ERRORS = {
  ro: {
    rate_limited: 'Prea multe audituri de pe această conexiune. Încearcă din nou într-un minut.',
    bad_request: 'Trimite JSON: {"url": "https://example.com"}',
    invalid_url: 'Aceasta nu pare o adresă publică de site.',
    unsupported_scheme: 'Pot audita doar site-uri http:// sau https://.',
    fetch_prefix: 'Nu am putut încărca acel site',
    fetch_suffix: 'Este online și public?',
    report_not_found: 'Acest link de audit a expirat sau nu a fost găsit. Rulează un audit nou mai jos.'
  },
  ru: {
    rate_limited: 'Слишком много аудитов с этого соединения. Попробуйте через минуту.',
    bad_request: 'Отправьте JSON: {"url": "https://example.com"}',
    invalid_url: 'Это не похоже на публичный адрес сайта.',
    unsupported_scheme: 'Аудит возможен только для сайтов http:// или https://.',
    fetch_prefix: 'Не удалось загрузить этот сайт',
    fetch_suffix: 'Он онлайн и публичный?',
    report_not_found: 'Ссылка на аудит устарела или не найдена. Запустите новый аудит ниже.'
  }
};

export function errMsg(key, lang, fallback) {
  return (ERRORS[lang] && ERRORS[lang][key]) || fallback;
}
