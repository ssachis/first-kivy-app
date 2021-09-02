

screen_helper="""
ScreenManager:
    MenuScreen:
    ProfileScreen:
    ListScreen:
<MenuScreen>:
    name:'menu'
    
    AnchorLayout:
        anchor_x: "center"
        size_hint_y: 1.6
        height: avatar.height
        Image:
            id: avatar
            size_hint: 0.5,0.5
            size: "56dp", "56dp"
            source: "C:/Users/sachi/OneDrive/Desktop/i.jpg"  
    
    MDTextField:
        hint_text: "Enter Username"
        helper_text:"or click on forgot username"
        helper_text_mode:"on_focus"
        icon_right:"android"
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{'center_x':0.5,'center_y':0.6}
        
        size_hint_x:None
        width:160
    MDTextField:
        hint_text: "Enter Password"
        helper_text:"or click on forgot password"
        helper_text_mode:"on_focus"
 
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:160
    MDRectangleFlatButton:
        text:'Next'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_press:root.manager.current='profile'
   
<ProfileScreen>:
    name:'profile'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Health App"
            elevation: 20
            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

        Widget:
        MDLabel:
            text:'hello user'
            halign:'center'
        
            
        MDRectangleFlatButton:
            text:'Back'
            pos_hint:{'center_x':0.5,'center_y':0.6 }
            on_press:root.manager.current='menu'
        MDRectangleFlatButton:
            text:'next'
            pos_hint:{'center_x':0.5,'center_y':0.5 }
            on_press:root.manager.current='list'
        
                    
        MDBottomAppBar:
            MDToolbar:
                          
                left_action_items:[["coffee",lambda x:app.navigation_draw()]]
                mode:'end'
                type:'bottom'
                elevation:40
            
                on_action_button:app.navigation_draw()
       
    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"
            AnchorLayout:
                anchor_x: "left"
                size_hint_y: None
                height: avatar.height

                Image:
                    id: avatar
                    size_hint: None,None
                    size: "56dp", "56dp"
                    source: "C:/Users/sachi/Music/i.png" 
               
       

            MDLabel:
                text: ' sachi'
                font_style: 'Button'
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: ' singhsachi.pratap1166@gmail.com'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                    

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'face-profile-woman'
                                
                    OneLineIconListItem:
                        text:'Upload'
                        IconLeftWidget:
                            icon:'file-upload'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'   
<ListScreen> :
    name:'list'
    ScrollView:
        MDList:
            id:container
     
                
               
            

        

"""


