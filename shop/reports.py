# import reporting
# from django.db.models import Sum, Avg, Count
# from models import Business,Customer,Product,Order,OrderItem

# class ProductReport(reporting.Report):
#     model = Product
#     verbose_name = 'product Report'
#     annotate = (                    # Annotation fields (tupples of field, func, title)
#         ('id', Count, 'Total'),     # example of custom title for column
#         ('price', Sum),            # no title - column will be "Salary Sum"
        
#     )
#     aggregate = (                   # columns that will be aggregated (syntax the same as for annotate)
#         ('id', Count, 'Total'),
#         ('price', Sum, 'revenue'),
#     )
#     group_by = [                   # list of fields and lookups for group-by options
#         'bsn_name',
#         'bsn_location',
#     ]
#     list_filter = [                # This are report filter options (similar to django-admin)
#        'price',
#     ]

#     # if detail_list_display is defined user will be able to see how rows was grouped
#     detail_list_display = [
#         'name',
#         'revenue',
#     ]

#     date_hierarchy = 'id' # the same as django-admin


# reporting.register('people', ProductReport) # Do not forget to 'register' your class in reports
