/**
 * Ámbito de cada referente, para el filtro de la página /referentes.
 * Se mantiene acá (y no en el frontmatter) para poder actualizarlo en un solo
 * lugar. Al agregar un referente nuevo, sumá su slug con su ámbito.
 * El filtro es client-side sobre tarjetas ya renderizadas → SEO-safe.
 */
export const AMBITOS = [
  "Tecnología",
  "Negocios e Inversión",
  "Escritores",
  "Psicología",
  "Entretenimiento",
  "Política y Sociedad",
  "Ciencia",
] as const;

export const ambitoDe: Record<string, string> = {
  "bill-gates": "Tecnología",
  "elon-musk": "Tecnología",
  "mark-zuckerberg": "Tecnología",
  "sam-altman": "Tecnología",
  "satya-nadella": "Tecnología",
  "andrew-ng": "Tecnología",
  "paul-graham": "Tecnología",
  "vitalik-buterin": "Tecnología",
  "lex-fridman": "Tecnología",

  "warren-buffett": "Negocios e Inversión",
  "jeff-bezos": "Negocios e Inversión",
  "richard-branson": "Negocios e Inversión",
  "ray-dalio": "Negocios e Inversión",
  "marc-andreessen": "Negocios e Inversión",
  "peter-thiel": "Negocios e Inversión",
  "naval-ravikant": "Negocios e Inversión",
  "simon-sinek": "Negocios e Inversión",
  "tim-ferriss": "Negocios e Inversión",
  "derek-sivers": "Negocios e Inversión",

  "yuval-noah-harari": "Escritores",
  "stephen-king": "Escritores",
  "j-k-rowling": "Escritores",
  "malcolm-gladwell": "Escritores",
  "nassim-nicholas-taleb": "Escritores",
  "ryan-holiday": "Escritores",
  "isabel-allende": "Escritores",
  "mario-vargas-llosa": "Escritores",

  "jordan-peterson": "Psicología",
  "adam-grant": "Psicología",
  "brene-brown": "Psicología",
  "angela-duckworth": "Psicología",
  "james-clear": "Psicología",

  "oprah-winfrey": "Entretenimiento",
  "emma-watson": "Entretenimiento",
  "natalie-portman": "Entretenimiento",
  "reese-witherspoon": "Entretenimiento",
  "gwyneth-paltrow": "Entretenimiento",
  "jenna-bush-hager": "Entretenimiento",

  "barack-obama": "Política y Sociedad",
  "malala-yousafzai": "Política y Sociedad",
  "garry-kasparov": "Política y Sociedad",

  "neil-degrasse-tyson": "Ciencia",
  "daniel-kahneman": "Ciencia",
};
