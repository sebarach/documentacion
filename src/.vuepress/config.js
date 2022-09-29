const { description } = require('../../package')

module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  dest:'docs',
  base:'/documentacion/',
  title: 'Documentacion Rapida',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,

  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    ['link', { rel: 'shortcut icon', type: "image/x-icon", href:`/favicon.ico` }]
  ],

  themeConfig: {
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: false,
    nav: [
      {
        text: 'React JS', 
        link: '/react/'
      },
      {
        text: 'Node JS', 
        link: '/nodejs/'
      },
      {
        text: 'Python', 
        link: '/python/'
      },
      {
        text: 'C-Sharp',
        link: '/guide/',
      }
    ],
    sidebar: {
      '/guide/': [
        {
          title: 'Guia',
          collapsable: true,
          children: [
            '',
            'InyeccionDependecy',
            'exception',
            'tips',
            'visualstudio',
          ]
        },
        {
            title:'MVC TIPS',
            collapsable:true,
            children: [
              '/guide/mvc/',
            ]
        }
      ],
    '/nodejs/':[
      {
        title:'General',
        collapsable: false
      },
      {
        title:'JavaScript',
        collapsable: true,
        children: [
          '/nodejs/javascript/',
          '/nodejs/javascript/modules',
        ]
      },
      {
        title:'NPM',
        collapsable: true
      },
      {
        title:'Express',
        collapsable: true
      },
      {
        title:'MySQL',
        collapsable: true
      },      
      {
        title:'PostgreSQL',
        collapsable: true
      }
    ],
    '/python/':[
      {
        title:'General',
        collapsable: false
      }
    ],
    '/react/':[
      {
        title:'General',
        collapsable: false
      }
    ],
    }
  },
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
  ]
}
