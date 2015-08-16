from base import QuickbooksBaseObject, Ref, CustomField, Address, EmailAddress, CustomerMemo, QuickbooksManagedObject
from tax import TxnTaxDetail


class DiscountLineDetail(QuickbooksBaseObject):
    class_dict = {
        "DiscountAccountRef": Ref
    }

    def __init__(self):
        super(DiscountLineDetail, self).__init__()
        self.PercentBased = True
        self.DiscountPercent = 0
        self.DiscountAccountRef = None

    def __unicode__(self):
        return self.DiscountPercent


class SalesItemLineDetail(QuickbooksBaseObject):
    class_dict = {
        "ItemRef": Ref,
        "TaxCodeRef": Ref
    }

    def __init__(self):
        super(SalesItemLineDetail, self).__init__()
        self.UnitPrice = 0
        self.Qty = 0

    def __unicode__(self):
        return self.UnitPrice


class InvoiceDetail(QuickbooksBaseObject):
    class_dict = {
        "DiscountLineDetail": DiscountLineDetail,
        "SalesItemLineDetail": SalesItemLineDetail,
    }

    def __init__(self):
        super(InvoiceDetail, self).__init__()
        self.LineNum = ""
        self.Description = ""
        self.Amount = ""
        self.DetailType = ""

    def __unicode__(self):
        return "[{0}] {1} {2}".format(self.LineNum, self.Description, self.Amount)

class Invoice(QuickbooksManagedObject):
    """
    QBO definition: An Invoice represents a sales form where the customer pays for a product or service later.

    """

    class_dict = {
        "DepartmentRef": Ref,
        "CurrencyRef": Ref,
        "CustomerRef": Ref,
        "ClassRef": Ref,
        "SalesTermRef": Ref,
        "ShipMethodRef": Ref,
        "DepositToAccountRef": Ref,
        "BillAddr": Address,
        "ShipAddr": Address,
        "TxnTaxDetail": TxnTaxDetail,
        "BillEmail": EmailAddress,
        "CustomerMemo": CustomerMemo
    }

    list_dict = {
        "CustomField": CustomField,
        "Line": InvoiceDetail
    }

    qbo_object_name = "Invoice"

    def __init__(self):
        super(Invoice, self).__init__()
        self.Deposit = 0
        self.Balance = 0
        self.AllowIPNPayment = True
        self.DocNumber = ""
        self.TxnDate = ""
        self.PrivateNote = ""
        self.DueDate = ""
        self.ShipDate = ""
        self.TrackingNum = ""
        self.TotalAmt = ""
        self.ApplyTaxAfterDiscount = ""
        self.PrintStatus = ""
        self.EmailStatus = ""

        self.BillAddr = None
        self.ShipAddr = None
        self.BillEmail = None
        self.CustomerRef = None
        self.CustomerMemo = None

        self.CustomField = []

    def __unicode__(self):
        return self.TotalAmt