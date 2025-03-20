from django.contrib.auth.models import Group, Permission

def create_groups_permissions(sender, **kwargs):
    try:
        readers_group, _ = Group.objects.get_or_create(name="Readers")
        authors_group, _ = Group.objects.get_or_create(name="Authors")
        editors_group, _ = Group.objects.get_or_create(name="Editors")
        
        readers_permission = [
            Permission.objects.get(codename="view_post")
        ]
        
        authors_permission = [
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post")
        ]
        
        can_publish_permission, _ = Permission.objects.get_or_create(
            codename="can_publish", content_type_id=8, name="Can publish Post"
        )
        
        editors_permission = [
            can_publish_permission,
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post")
        ]
        
        readers_group.permissions.set(readers_permission)
        authors_group.permissions.set(authors_permission)
        editors_group.permissions.set(editors_permission)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("Groups and Permissions created successfully")

