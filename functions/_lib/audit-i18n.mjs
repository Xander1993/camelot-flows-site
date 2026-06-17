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
    lcp: { title: 'Conținutul principal apare în {secs}s (LCP)', detail: 'Largest Contentful Paint peste 4 secunde este în banda „slabă” a Google, afectează atât pozițiile, cât și răbdarea.' }
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
    lcp: { title: 'Основной контент появляется за {secs}с (LCP)', detail: 'Largest Contentful Paint выше 4 секунд в «плохой» зоне Google, это бьёт и по позициям, и по терпению.' }
  }
};

function interp(s, vars) {
  if (!vars) return s;
  return s.replace(/\{(\w+)\}/g, (m, k) => (k in vars && vars[k] != null ? String(vars[k]) : m));
}

export function localizeFindings(findings, lang) {
  const dict = FINDINGS[lang];
  if (!dict) return findings;
  return findings.map((x) => {
    const t = dict[x.id];
    if (!t) return x; // EN fallback for any id not yet translated
    return { id: x.id, severity: x.severity, title: interp(t.title, x.vars), detail: interp(t.detail, x.vars), vars: x.vars };
  });
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
    fetch_prefix: 'Nu am putut încărca acel site',
    fetch_suffix: 'Este online și public?'
  },
  ru: {
    rate_limited: 'Слишком много аудитов с этого соединения. Попробуйте через минуту.',
    bad_request: 'Отправьте JSON: {"url": "https://example.com"}',
    invalid_url: 'Это не похоже на публичный адрес сайта.',
    fetch_prefix: 'Не удалось загрузить этот сайт',
    fetch_suffix: 'Он онлайн и публичный?'
  }
};

export function errMsg(key, lang, fallback) {
  return (ERRORS[lang] && ERRORS[lang][key]) || fallback;
}
