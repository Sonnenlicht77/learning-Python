import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    base:"/learning-Python/",
  title: "Learning Python",
  description: "A VitePress Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '语法基础', link: '/01_base_py/index' },
      { text: '爬虫' , link:'/02_crawler_py/index'}
    ],

    sidebar:{
        '/01_base_py':[
            {
                text: '语法基础',
                base:'/01_base_py',
                link:'/index'
                items:[
                    {
                        text:'数据类型',
                        link:'/01.数据类型.md'
                    }
                ]
            }
        ],
      '/02_crawler_py':[
        {
             text:'爬虫',
             link:'/index',
             base:'/02_crawler_py',
             items:[
                {
                    text:'urllib',
                    link:'/01.urllib'
                }
             ]
        }
     ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
