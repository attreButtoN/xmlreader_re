from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to="documents/%Y/%m/%d")
    xmlfile = models.FileField(upload_to="documents/%Y/m/%d")


class Sro(models.Model):
    sro_name = models.CharField(max_length=512, blank=False, verbose_name="SroName")
    sro_registry_number = models.CharField(
        max_length=30, blank=False, verbose_name="SroRegistryNumber"
    )
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")
    legal_address = models.CharField(
        max_length=1024, blank=True, verbose_name="LegalAddress"
    )


class AdditionalInfo(models.Model):
    nil = models.BooleanField(null=True, blank=True, verbose_name="nil")

    def __bool__(self):
        return self.nil


class AnullmentMessage(models.Model):
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    id_annulment = models.IntegerField(
        null=True, blank=True, verbose_name="ID_Annulment"
    )
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    is_hide = models.BooleanField(null=True, blank=True, verbose_name="IsHide")

    def __str__(self):
        return f"{self.event_time} {self.trade_id} {self.id_annulment} {self.reason}{self.is_hide}"


class Application(models.Model):
    time_begin = models.DateTimeField(null=True, blank=True, verbose_name="TimeBegin")
    time_end = models.DateTimeField(null=True, blank=True, verbose_name="TimeEnd")
    cause_of_refuse = models.TextField(
        null=True, blank=True, verbose_name="CauseOfRefuse"
    )
    rules = models.TextField(null=True, blank=True, verbose_name="Rules")

    def __str__(self):
        return f"{self.time_begin} {self.cause_of_refuse} {self.rules}"


class ApplicationData(models.Model):
    result = models.TextField(null=True, blank=True, verbose_name="Result")
    cause_of_refuse = models.TextField(
        null=True, blank=True, verbose_name="CauseOfRefuse"
    )

    def __str__(self):
        return self.result, self.cause_of_refuse


class ArbitrManager(models.Model):
    inn = models.TextField(max_length=12, null=True, blank=True, verbose_name="INN")
    sro = models.ForeignKey(Sro, blank=False, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=50, blank=False, null=True, verbose_name="FirstName"
    )
    last_name = models.CharField(
        max_length=50, blank=False, null=True, verbose_name="LastName"
    )
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    reg_num = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="RegNum"
    )
    ogrn = models.CharField(max_length=15, blank=True, null=True, verbose_name="OGRNIP")
    snils = models.CharField(max_length=11, blank=True, null=True, verbose_name="SNILS")
    correspodence_address = models.CharField(
        max_length=300, blank=True, null=True, verbose_name="CorrespodenceAddress"
    )

    def __str__(self):
        return f"{self.inn} {self.sro} {self.first_name} {self.last_name} {self.middle_name}{self.reg_num}"


class Attach(models.Model):
    # id = models.IntegerField(primary_key=True)
    file_name = models.TextField(null=True, blank=True, verbose_name="FileName")
    type = models.TextField(null=True, blank=True, verbose_name="Type")
    blob = models.TextField(null=True, blank=True, verbose_name="Blob")

    def __str__(self):
        return f"{self.file_name} {self.type} {self.blob}"


class BankruptcyCreditorCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")

    def __str__(self):
        return f"{self.full_name} {self.short_name}"


class BankruptcyCreditorPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class BiddingStateLotInfo(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")

    def __str__(self):
        return f"{self.lot_number} {self.reason}"


class BuyerCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.IntegerField(null=True, blank=True, verbose_name="ORGN")
    legal_address = models.TextField(null=True, blank=True, verbose_name="LegalAddress")
    post_address = models.TextField(null=True, blank=True, verbose_name="PostAddress")
    phone = models.IntegerField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")


class BuyerPerson(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrnip = models.TextField(null=True, blank=True, verbose_name="OGRNIP")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")

    def __str__(self):
        return f"{self.full_name} {self.last_name} {self.middle_name} {self.inn} {self.ogrnip} {self.address} {self.phone} {self.email}"


class Classification(models.Model):
    idclass = models.TextField(null=True, verbose_name="IDClass")

    def __int__(self):
        return self.idclass


class CloseForm(models.Model):
    time_result = models.DateTimeField(null=True, blank=True, verbose_name="TimeResult")

    def __str__(self):
        return self.time_result


class CompanyBankrCommis(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")

    def __str__(self):
        return f"{self.full_name} {self.short_name}{self.inn}{self.ogrn}"


# class ContractNumber(models.Model):
#     nil = models.TextField(null=True)
#
#     def __bool__(self):
#         return self.nil


class ContractParticipant(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name="Name")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    is_winner = models.BooleanField(null=True, blank=True, verbose_name="IsWinner")
    is_buyer = models.BooleanField(null=True, blank=True, verbose_name="IsBuyer")

    def __str__(self):
        return f"{self.name} {self.ogrn} {self.inn} {self.is_winner} {self.is_buyer}"


class CreditorLotNumber(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")

    def __int__(self):
        return self.lot_number


class DatePublishSmi(models.Model):
    nil = models.BooleanField(null=True, blank=True)

    def __bool__(self):
        return self.nil


class DebtorCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")

    def __str__(self):
        return f"{self.full_name} {self.short_name} {self.inn}{self.ogrn}"


class DeptorPerson(models.Model):
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    snils = models.TextField(null=True, blank=True, verbose_name="SNILS")
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")

    def __str__(self):
        return f"{self.inn} {self.snils} {self.first_name}{self.last_name}{self.middle_name}"


class Information(models.Model):
    nil = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nil


class LegalCase(models.Model):
    case_number = models.TextField(null=True, blank=True, verbose_name="CaseNumber")
    court_name = models.TextField(null=True, blank=True, verbose_name="CourtName")
    base = models.TextField(null=True, blank=True, verbose_name="Base")

    def __str__(self):
        return f"{self.case_number} {self.court_name} {self.base}"


class LotInfo(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")

    def __int__(self):
        return self.lot_number


class OpenForm(models.Model):
    time_begin = models.DateTimeField(null=True, blank=True, verbose_name="TimeBegin")
    time_end = models.DateTimeField(null=True, blank=True, verbose_name="TimeEnd")

    def __str__(self):
        return f"{self.time_begin}{self.time_end}"


class ParticipantCompany(models.Model):
    legal_address = models.TextField(null=True, blank=True, verbose_name="LegalAddress")
    post_address = models.TextField(null=True, blank=True, verbose_name="PostAddress")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")
    full_name = models.TextField(null=True, blank=True, verbose_name="Phone")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.IntegerField(null=True, blank=False, verbose_name="ORGN")

    def __str__(self):
        return (
            f"{self.legal_address} {self.post_address} {self.phone} {self.email} {self.full_name}"
            f" {self.short_name} "
            f"{self.inn} {self.ogrn} "
        )


class ParticipantPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrnip = models.IntegerField(null=True, blank=True, verbose_name="OGRNIP")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")


class PriceInfo(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")
    new_price = models.FloatField(null=True, blank=True, verbose_name="NewPrice")

    def __str__(self):
        return self.lot_number, self.new_price


class StepPrice(models.Model):
    nil = models.BooleanField(null=True, blank=True)

    def __bool__(self):
        return self.nil


class TradeOrganizerCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")
    is_asv = models.BooleanField(null=True, blank=True, verbose_name="IsAsv")

    def __str__(self):
        return f"{self.full_name} {self.short_name} {self.inn} {self.inn} {self.ogrn} {self.is_asv}"


class TradeOrganizerPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FistName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    snils = models.TextField(null=True, blank=True, verbose_name="SNILS")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name} {self.inn} {self.snils}"


class WinnerCompany(models.Model):
    legal_address = models.TextField(null=True, blank=True, verbose_name="LegalAddress")
    post_address = models.TextField(null=True, blank=True, verbose_name="PostAdress")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="OGRN")

    def __str__(self):
        return f"{self.legal_address} {self.post_address} {self.phone} {self.email} {self.full_name} {self.short_name} {self.inn} {self.ogrn}"


class WinnerPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrnip = models.TextField(null=True, blank=True, verbose_name="OGRNIP")
    snils = models.TextField(null=True, blank=True, verbose_name="SNILS")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name}{self.middle_name}{self.inn} {self.ogrnip} {self.snils} {self.address} {self.phone} {self.email}"


class ApplicationList(models.Model):
    applications_data = models.ForeignKey(
        ApplicationData,null=True, verbose_name="ApplicationData", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.applications_data


class BiddingProcessInfo(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    price_info = models.ForeignKey(
        PriceInfo, on_delete=models.CASCADE,null=True, verbose_name="PriceInfo"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.price_info}"


class ContractInfo(models.Model):
    contract_number = models.TextField(
        null=True,
        blank=True,
        verbose_name="ContractNumber",
    )
    nil = models.BooleanField(null=True, blank=True, verbose_name="nil")
    date_contract = models.DateTimeField(
        null=True, blank=True, verbose_name="DateContract"
    )
    price = models.FloatField(null=True, blank=True, verbose_name="Price")

    def __str__(self):
        return f"{self.contract_number} {self.nil} {self.date_contract} {self.price}"


class ContractParticipantList(models.Model):
    contract_participant = models.ForeignKey(
        ContractParticipant,
        on_delete=models.CASCADE,
        verbose_name="ContractParticipant",
        null=True,
    )

    def __str__(self):
        return self.contract_participant


class CreditorLotNumberList(models.Model):
    creditor_lot_number = models.ForeignKey(
        CreditorLotNumber, on_delete=models.CASCADE, null=True,verbose_name="CreditorLotNumber"
    )

    def __str__(self):
        return self.creditor_lot_number


class Debtor(models.Model):
    debtor_company = models.ForeignKey(
        DebtorCompany, on_delete=models.CASCADE, null=True,verbose_name="DebtorCompany"
    )
    debtor_person = models.ForeignKey(
        DeptorPerson, on_delete=models.CASCADE, null=True,verbose_name="DebtorPerson"
    )

    def __str__(self):
        return f"{self.debtor_company}{self.debtor_person}"


class FailureTradeResult(models.Model):
    substantiation = models.TextField(
        null=True, blank=True, verbose_name="Substantiation"
    )
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    buyer_company = models.ForeignKey(
        BuyerCompany, on_delete=models.CASCADE,null=True, verbose_name="BuyerCompany"
    )
    buyer_person = models.ForeignKey(
        BuyerPerson, on_delete=models.CASCADE,null=True, verbose_name="BuyerPerson"
    )

    def __str__(self):
        return f"{self.substantiation} {self.price} {self.buyer_company} {self.buyer_person}"


class Lot(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")
    start_price = models.FloatField(null=True, blank=True, verbose_name="StartPrice")
    step_price = models.ForeignKey(
        StepPrice, on_delete=models.CASCADE, null=True,verbose_name="StepPrice"
    )
    step_price_percent = models.FloatField(
        null=True, blank=True, verbose_name="StepPricePercent"
    )
    price_reduction = models.TextField(
        null=True, blank=True, verbose_name="PriceReduction"
    )
    participants = models.TextField(null=True, blank=True, verbose_name="Participants")
    advance = models.FloatField(null=True, blank=True, verbose_name="Advance")
    trade_object_html = models.TextField(
        null=True, blank=True, verbose_name="TradeObjectHtml"
    )
    advance_percent = models.FloatField(
        null=True, blank=True, verbose_name="AdvancePercent"
    )
    concours = models.TextField(null=True, blank=True, verbose_name="Concours")
    payment_info = models.TextField(null=True, blank=True, verbose_name="PaymentInfo")
    sale_agreement = models.TextField(
        null=True, blank=True, verbose_name="SaleAgreement"
    )
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE,null=True, verbose_name="Classification"
    )


class Participant(models.Model):
    participant_person = models.ForeignKey(
        ParticipantPerson, on_delete=models.CASCADE, null=True,verbose_name="ParticipantPerson"
    )
    participant_company = models.ForeignKey(
        ParticipantCompany, on_delete=models.CASCADE,null=True, verbose_name="ParticipantCompany"
    )

    def __str__(self):
        return f"{self.participant_person}{self.participant_company}"


class SetAnnulment(models.Model):
    annulment_message = models.ForeignKey(
        AnullmentMessage,null=True, on_delete=models.CASCADE,verbose_name="AnnulmentMessage"
    )

    def __str__(self):
        return self.annulment_message


class SuccessTradeResult(models.Model):
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    substantiation = models.TextField(
        null=True, blank=True, verbose_name="Substantiation"
    )
    winner_person = models.ForeignKey(
        WinnerPerson, on_delete=models.CASCADE,null=True, verbose_name="WinnerPerson"
    )
    winner_company = models.ForeignKey(
        WinnerCompany, on_delete=models.CASCADE,null=True, verbose_name="WinnerCompany"
    )

    def __str__(self):
        return f"{self.price} {self.substantiation} {self.winner_person} {self.winner_company}"


class TradeOrganizer(models.Model):
    trade_organizer_person = models.ForeignKey(
        TradeOrganizerPerson,
        on_delete=models.CASCADE,
        verbose_name="TradeOgranizerPerson",
        null=True,
    )
    trade_organizer_company = models.ForeignKey(
        TradeOrganizerCompany,
        on_delete=models.CASCADE,
        verbose_name="TradeOrganizerCompany",
        null=True,
    )

    def __str__(self):
        return f"{self.trade_organizer_person}{self.trade_organizer_company}"


class BankruptcyCreditor(models.Model):
    bankruptcy_creditor_person = models.ForeignKey(
        BankruptcyCreditorPerson,
        on_delete=models.CASCADE,
        verbose_name="BankruptcyCreditorCompany",
        null=True,
    )
    bankruptcy_creditor_company = models.ForeignKey(
        BankruptcyCreditorCompany,
        on_delete=models.CASCADE,
        verbose_name="BankruptcyCreditorCompany",
        null=True,
    )
    creditor_lot_number_list = models.ForeignKey(
        CreditorLotNumberList,
        on_delete=models.CASCADE,
        verbose_name="CreditorLotNumberList",
        null=True,
    )

    def __str__(self):
        return f"{self.bankruptcy_creditor_person} {self.bankruptcy_creditor_company} {self.creditor_lot_number_list}"


class LotContractSale(models.Model):
    lot_number = models.IntegerField(blank=True, null=True, verbose_name="LotNumber")
    contract_info = models.ForeignKey(
        ContractInfo, on_delete=models.CASCADE,null=True, verbose_name="LotNumber"
    )
    contract_participant = models.ForeignKey(
        ContractParticipantList,
        on_delete=models.CASCADE,
        verbose_name="ContractParticipantList",
        null=True,
    )
    additional_info = models.ForeignKey(
        AdditionalInfo, on_delete=models.CASCADE,null=True, verbose_name="AdditionalInfo"
    )

    def __str__(self):
        return f"{self.lot_number} {self.contract_info} {self.contract_participant} {self.additional_info}"


class LotStatistic(models.Model):
    lot_number = models.IntegerField(blank=True, null=True, verbose_name="LotNumber")
    entry_count = models.IntegerField(blank=True, null=True, verbose_name="EntryCount")
    accept_count = models.IntegerField(
        blank=True, null=True, verbose_name="AcceptCount"
    )
    application_list = models.ForeignKey(
        ApplicationList, on_delete=models.CASCADE,null = True, verbose_name="ApplicationList"
    )

    def __str__(self):
        return f"{self.lot_number} {self.entry_count} {self.accept_count} {self.application_list}"


class Participants(models.Model):
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE,null=True, verbose_name="Participant"
    )

    def __str__(self):
        return self.participant


class SetBiddingProcessInfo(models.Model):
    bidding_process_info = models.ForeignKey(
        BiddingProcessInfo,null=True, on_delete=models.CASCADE, verbose_name="BiddingProcessInfo"
    )

    def __str__(self):
        return self.bidding_process_info


class BankruptcyCreditorList(models.Model):
    bankruptcy_creditor = models.ForeignKey(
        BankruptcyCreditor, null=True,on_delete=models.CASCADE, verbose_name="BankruptcyCreditor"
    )

    def __str__(self):
        return self.bankruptcy_creditor


class LotContractSaleList(models.Model):
    lot_contract_sale = models.ForeignKey(
        LotContractSale,null=True, on_delete=models.CASCADE, verbose_name="LotContractSale"
    )

    def __str__(self):
        return self.lot_contract_sale


class LotTradeResult(models.Model):
    lot_number = models.IntegerField(blank=True, null=True, verbose_name="LotNumber")
    success_trade_result = models.ForeignKey(
        SuccessTradeResult, null=True,on_delete=models.CASCADE, verbose_name="SuccesTradeResult"
    )
    failure_trade_result = models.ForeignKey(
        FailureTradeResult,null=True, on_delete=models.CASCADE, verbose_name="FailureTradeResult"
    )
    participants = models.ForeignKey(
        Participants,null=True, on_delete=models.CASCADE, verbose_name="Participants"
    )

    def __str__(self):
        return f"{self.lot_number} {self.success_trade_result} {self.failure_trade_result} {self.participants}"


class BiddingEndBankruptcyCreditor(models.Model):
    trade_id = models.TextField(blank=True, null=True, verbose_name="TradeId")
    event_time = models.DateTimeField(blank=True, null=True, verbose_name="EventTime")
    bankruptcy_creditor_list = models.ForeignKey(
        BankruptcyCreditorList,
        on_delete=models.CASCADE,
        verbose_name="BankruptcyCreditorList",
    )
    information = models.ForeignKey(
        Information,null=True, on_delete=models.CASCADE, verbose_name="Information"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.bankruptcy_creditor_list} {self.information}"


class ContractSale(models.Model):
    trade_id = models.TextField(blank=True, null=True, verbose_name="TradeId")
    event_time = models.DateTimeField(blank=True, null=True, verbose_name="EventTime")
    lot_contract_sale_list = models.ForeignKey(
        LotContractSaleList,
        on_delete=models.CASCADE,
        verbose_name="LotContractSaleList",
        null=True,
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_contract_sale_list}"


class LotList(models.Model):
    lot = models.ForeignKey(Lot,null=True, on_delete=models.CASCADE, verbose_name="Lot")
    lot_statistic = models.ForeignKey(
        LotStatistic, on_delete=models.CASCADE,null=True, verbose_name="LotStatistic"
    )
    bidding_state_lot_info = models.ForeignKey(
        BiddingStateLotInfo, on_delete=models.CASCADE,null=True, verbose_name="LotStatistic"
    )
    lot_trade_result = models.ForeignKey(
        LotTradeResult, on_delete=models.CASCADE,null=True, verbose_name="LotTradeResult"
    )
    lot_info = models.ForeignKey(
        LotInfo, on_delete=models.CASCADE, null=True,verbose_name="LotInfo"
    )
    nil = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.lot}{self.lot_statistic}{self.bidding_state_lot_info} {self.lot_trade_result} {self.lot_info} {self.nil}"


class ApplicationSessionEnd(models.Model):
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    lot_list = models.ForeignKey(
        LotList, null=True,on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.event_time}{self.trade_id}{self.lot_list}"


class ApplicationSessionStart(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList,null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id}{self.event_time}{self.lot_list}"


class ApplicationSessionStatistic(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    date_begin = models.DateTimeField(null=True, blank=True, verbose_name="DateBegin")
    lot_list = models.ForeignKey(
        LotList,null=True, on_delete=models.CASCADE, verbose_name="LotList",blank=True,
    )
    attach = models.ForeignKey(Attach,null=True, on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list} {self.attach}"


class BiddingCancel(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    lot_list = models.ForeignKey(
        LotList,null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.reason} {self.lot_list}"


class BiddingEnd(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList,null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list}"


class BiddingFail(models.Model):
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, null=True,on_delete=models.CASCADE, verbose_name="LotList"
    )
    attach = models.ForeignKey(Attach,null=True, on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return f"{self.reason} {self.trade_id} {self.event_time} {self.lot_list} {self.attach}"


class BiddingPause(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    lot_list = models.ForeignKey(
        LotList,null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.reason} {self.lot_list}"


class BiddingResult(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE,null=True, verbose_name="LotList"
    )
    attach = models.ForeignKey(Attach, null=True,on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list} {self.attach}"

# class SetBiddingResult(models.Model):
#
#     bidding_result = models.ForeignKey(BiddingResult,null=True,on_delete=models.CASCADE,verbose_name="BiddingResult")


class BiddingResume(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE,null=True, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.reason} {self.lot_list}"


class BiddingStart(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE, null=True,verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list}"


class SetBiddingEndBankruptcyCreditor(models.Model):
    bidding_end_bankruptcy_creditor = models.ForeignKey(
        BiddingEndBankruptcyCreditor,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="BiddingEndBankruptcyCreditor",
    )

    def __str__(self):
        return self.bidding_end_bankruptcy_creditor


class SetContractSale(models.Model):
    contract_sale = models.ForeignKey(
        ContractSale,null=True, on_delete=models.CASCADE, verbose_name="ContractSale"
    )

    def __str__(self):
        return self.contract_sale


class TradeInfo(models.Model):
    auction_type = models.TextField(null=True, blank=True, verbose_name="AuctionType")
    form_price = models.TextField(null=True, blank=True, verbose_name="FormPrice")
    isrepeat = models.BooleanField(null=True, blank=True, verbose_name="ISRepeat")
    close_form = models.ForeignKey(
        CloseForm,null=True, on_delete=models.CASCADE, verbose_name="CloseForm"
    )
    date_publish_smi = models.ForeignKey(
        DatePublishSmi,null=True, on_delete=models.CASCADE, verbose_name="DatePublishSMI"
    )
    date_publish_efir = models.DateTimeField(
        null=True, blank=True, verbose_name="DatePublishEFIR"
    )
    open_form = models.ForeignKey(
        OpenForm, on_delete=models.CASCADE, null=True,verbose_name="OpenForm"
    )
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE,null=True, verbose_name="Application"
    )
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE,null=True, verbose_name="LotList"
    )
    attach = models.ForeignKey(Attach, null=True,on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return (
            f"{self.auction_type} {self.form_price} "
            f"{self.isrepeat} {self.close_form} {self.date_publish_smi} "
            f"{self.date_publish_efir} {self.open_form}{self.application}{self.lot_list}{self.attach}"
        )


class BiddingInvitation(models.Model):
    trade_id = models.TextField(blank=True, null=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    idefrsb = models.TextField(null=True, blank=True, verbose_name="IDEFRSB")
    debtor = models.ForeignKey(Debtor,null=True, on_delete=models.CASCADE, verbose_name="Debtor")
    legal_case = models.ForeignKey(
        LegalCase, on_delete=models.CASCADE,null=True, verbose_name="LegalCase"
    )
    company_bankr_commis = models.ForeignKey(
        CompanyBankrCommis, on_delete=models.CASCADE,null=True, verbose_name="CompanyBankrCommis"
    )
    arbitr_manager = models.ForeignKey(
        ArbitrManager, on_delete=models.CASCADE,null=True, verbose_name="ArbitrManager"
    )
    trade_ogranizer = models.ForeignKey(
        TradeOrganizer, on_delete=models.CASCADE,null=True, verbose_name="TradeOrganizer"
    )
    trade_info = models.ForeignKey(
        TradeInfo, on_delete=models.CASCADE,null=True, verbose_name="TradeInfo"
    )
    def __str__(self):
        return (
            f"{self.trade_id} {self.event_time} "
            f"{self.idefrsb} {self.debtor} {self.legal_case} "
            f"{self.company_bankr_commis} {self.arbitr_manager}{self.trade_ogranizer}{self.trade_info}")




class SetApplicationSessionEnd(models.Model):
    application_session_end = models.ForeignKey(
        ApplicationSessionEnd,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="ApplicationSessionEnd",
    )

    def __str__(self):
        return self.application_session_end


class SetApplicationSessionStart(models.Model):
    application_session_start = models.ForeignKey(
        ApplicationSessionStart,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="ApplicationSessionStart",
    )

    def __str__(self):
        return self.application_session_start


class SetApplicationSessionStatistic(models.Model):
    application_session_statistic = models.ForeignKey(
        ApplicationSessionStatistic,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="ApplicationSessionStatistic",
    )

    def __str__(self):
        return self.application_session_statistic


class SetBiddingCancel(models.Model):
    bidding_cancel = models.ForeignKey(
        BiddingCancel,null=True, on_delete=models.CASCADE, verbose_name="BiddingCancel"
    )

    def __str__(self):
        return self.bidding_cancel


class SetBiddingEnd(models.Model):
    bidding_end = models.ForeignKey(
        BiddingEnd,null=True, on_delete=models.CASCADE, verbose_name="BiddingEnd"
    )

    def __str__(self):
        return self.bidding_end


class SetBiddingFail(models.Model):
    bidding_fail = models.ForeignKey(
        BiddingFail,null=True, on_delete=models.CASCADE, verbose_name="BiddingFail"
    )

    def __str__(self):
        return self.bidding_fail


class SetBiddingPause(models.Model):
    bidding_pause = models.ForeignKey(
        BiddingPause,null=True, on_delete=models.CASCADE, verbose_name="BiddingPause"
    )

    def __str__(self):
        return self.bidding_pause


class SetBiddingResult(models.Model):
    bidding_result = models.ForeignKey(
        BiddingResult, null=True,on_delete=models.CASCADE, verbose_name="BiddingResult"
    )

    def __str__(self):
        return self.bidding_result


class SetBiddingResume(models.Model):
    bidding_resume = models.ForeignKey(
        BiddingResume,null=True, on_delete=models.CASCADE, verbose_name="BiddingResume"
    )

    def __str__(self):
        return self.bidding_resume


class SetBiddingStart(models.Model):
    bidding_start = models.ForeignKey(
        BiddingStart,null=True, on_delete=models.CASCADE, verbose_name="BiddingStart"
    )

    def __str__(self):
        return self.bidding_start


class SetBiddingInvitation(models.Model):
    bidding_invitations = models.ForeignKey(
        BiddingInvitation,null=True, on_delete=models.CASCADE, verbose_name="BiddingInvitation"
    )

    def __str__(self):
        return self.bidding_invitations


class Body(models.Model):
    set_bidding_process_info = models.ForeignKey(
        SetBiddingProcessInfo,
        on_delete=models.CASCADE,
        verbose_name="SetBiddingProcessInfo",
        null=True,
    )
    set_application_session_start = models.ForeignKey(
        SetApplicationSessionStart,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetApplicationSessionStart",
    )
    set_application_session_end = models.ForeignKey(
        SetApplicationSessionEnd,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetApplicationSessionEnd",
    )
    set_application_session_statistic = models.ForeignKey(
        SetApplicationSessionStatistic,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetApplicationSessionStatistic",
    )
    set_bidding_fail = models.ForeignKey(
        SetBiddingFail,null=True, on_delete=models.CASCADE, verbose_name="SetBiddingFail"
    )
    set_bidding_invitation = models.ForeignKey(
        SetBiddingInvitation,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetBiddingInvitation",
    )
    set_contract_sale = models.ForeignKey(
        SetContractSale,null=True, on_delete=models.CASCADE, verbose_name="SetContractSale"
    )
    set_bidding_result = models.ForeignKey(
        SetBiddingResult, null=True,on_delete=models.CASCADE, verbose_name="SetBuddingResult"
    )

    set_bidding_end = models.ForeignKey(
        SetBiddingEnd,null=True, on_delete=models.CASCADE, verbose_name="SetBiddingEnd"
    )

    set_bidding_start = models.ForeignKey(
        SetBiddingStart, null=True,on_delete=models.CASCADE, verbose_name="SetBiddingStart"
    )

    set_bidding_cancel = models.ForeignKey(
        SetBiddingCancel, null=True,on_delete=models.CASCADE, verbose_name="SetBiddingCancel"
    )
    set_bidding_pause = models.ForeignKey(
        SetBiddingPause, null=True,on_delete=models.CASCADE, verbose_name="SetBiddingPause"
    )
    set_annulment = models.ForeignKey(
        SetAnnulment,null=True, on_delete=models.CASCADE, verbose_name="SetAnnulment"
    )
    set_bidding_end_bankruptcy_creditor = models.ForeignKey(
        SetBiddingEndBankruptcyCreditor,
        on_delete=models.CASCADE,
        verbose_name="set_bidding_end_bankruptcy_creditor",
        null =True,
    )
    set_bidding_resume = models.ForeignKey(
        SetBiddingResume,null=True, on_delete=models.CASCADE, verbose_name="SetBiddingResume"
    )

    def __str__(self):
        return (
            f"{self.set_bidding_process_info}{self.set_application_session_start}{self.set_application_session_end}"
            f"{self.set_application_session_statistic}{self.set_bidding_fail}{self.set_bidding_invitation}"
            f"{self.set_contract_sale}{self.set_bidding_result}{self.set_bidding_end}"
            f"{self.set_bidding_start}{self.set_bidding_cancel}{self.set_bidding_cancel}"
            f"{self.set_bidding_pause}{self.set_annulment}"
            f"{self.set_bidding_end_bankruptcy_creditor}{self.set_bidding_resume}"
        )


class Envelope(models.Model):
    body = models.ForeignKey(Body,null=True, on_delete=models.CASCADE, verbose_name="Body")

    # w3_org_2003_05_soap_envelope_body = models.ForeignKey(Body, on_delete=models.CASCADE, verbose_name="Body",related_name="w3_body")

    def __str__(self):
        return f"{self.body}"


class Message(models.Model):
    # id = models.IntegerField(primary_key=True,null= True, verbose_name="ID")
    envelope = models.ForeignKey(
        Envelope,null=True, on_delete=models.CASCADE, verbose_name="Envelope"
    )

    # w3_org_2003_05_soap_envelope_envelope = models.ForeignKey(Envelope, on_delete=models.CASCADE,
    #                                                           verbose_name="Envelope")

    def __str__(self):
        return (
            f"{self.envelope}"
            """{self.w3_org_2003_05_soap_envelope_envelope}"""
        )


class Trade(models.Model):
    id_efrsb = models.IntegerField(null=True, blank=True, verbose_name="ID_EFRSB")
    id_external = models.TextField(null=True, blank=True, verbose_name="ID_External")
    message = models.ForeignKey(
        Message, null=True,on_delete=models.CASCADE, verbose_name="Message"
    )


class TradeList(models.Model):
    trade = models.ForeignKey(Trade,null=True, on_delete=models.CASCADE, verbose_name="Trade")


class TradePlace(models.Model):
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    trade_list = models.ForeignKey(
        TradeList,null = True, on_delete=models.CASCADE, verbose_name="TradeList"
    )


class TradePlaceList(models.Model):
    trade_place = models.ForeignKey(
        TradePlace,null=True, on_delete=models.CASCADE, verbose_name="TradeList"
    )


# ============================================================================================


# class GetMessageContent(models.Model):
#     id = models.IntegerField(primary_key=True, blank=False, null=False, verbose_name="Идентификатор сообщения в ЕФРСБ")
#
#
# class GetDebtorMessagesContentForPeriodByIdBankrupt(models.Model):
#     IdBankrupt = models.IntegerField(primary_key=True, blank=False, null=False, verbose_name="Идентификатор должника")
#     startDate = models.DateTimeField(blank=True, null=True, verbose_name="Дата начала периода")
#
#
# class FirmTradeOrganizerAgent(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=False, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#     firm_trade_organizer = models.ForeignKey(FirmTradeOrganizer, blank=False, verbose_name="FirmTradeOrganizer",
#                                              on_delete=models.CASCADE)
#
#
# class FirmTradeOrganizer(models.Model):
#     full_name = models.CharField(max_length=1024, blank=False, verbose_name="FullName")
#     short_name = models.CharField(max_length=512, blank=False, verbose_name="ShortName")
#     post_address = models.CharField(max_length=300, blank=False, verbose_name="PostAddress")
#     legal_address = models.CharField(max_length=300, blank=False, verbose_name="LegalAddress")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRN")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#     okpo = models.CharField(max_length=8, blank=False, verbose_name="OKPO")
#
#
# class SroInfo(models.Model):
#     inn = models.CharField(max_length=15, blank=False, verbose_name="INN")
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRN")
#     legal_address = models.CharField(max_length=1024, blank=False, verbose_name="LegalAddress")
#     post_address = models.CharField(max_length=1024, blank=False, verbose_name="PostAddress")
#
#
# class OperatorSro(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=False, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#     sro_info = models.ForeignKey(SroInfo, blank=False, verbose_name="SroInfo", on_delete=models.CASCADE)
#
#
# class PersonTradeOrganizer(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=False, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#     address = models.CharField(max_length=300, blank=False, verbose_name="Address")
#     inn = models.CharField(max_length=12, blank=False, verbose_name="INN")
#     ogrnip = models.CharField(max_length=15, blank=False, verbose_name="OGRNIP")
#
#
# class ForeignSystem(models.Model):
#     name = models.CharField(max_length=256, blank=False, verbose_name="Name")
#
#
# class Operator(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#     organization_name = models.CharField(max_length=50, blank=False, verbose_name="OrganizationName")
#     organization_department_name = models.CharField(max_length=200, blank=False,
#                                                     verbose_name="OrganizationDepartmentName")
#
#
# class FnsDepartment(models.Model):
#     name = models.CharField(max_length=250, blank=False, verbose_name="Name")
#     inn = models.CharField(max_length=12, blank=False, verbose_name="INN")
#
#
# class Person(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#     inn = models.CharField(max_length=12, blank=False, verbose_name="INN")
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=1024, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRN")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Fio(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#
#
# class Publisher_Arbitr_Manager_v2(models.Model):
#     fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=False)
#     inn = models.CharField(max_length=12, blank=False, verbose_name="INN")
#     snils = models.CharField(max_length=11, blank=False, verbose_name="SNILS")
#     ogrnip = models.CharField(max_length=15, blank=True, verbose_name="OGRNIP")
#     correspondence_address = models.CharField(max_length=300, blank=False, verbose_name="Correspondence Address")
#     sro = models.ForeignKey(Sro, on_delete=models.CASCADE, blank=True)
#
#
# class Publisher_Arbitr_Manager_Sro_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRN")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#     address = models.CharField(max_length=1024, blank=False, verbose_name="Address")
#
#
# class Publisher_FirmTrade_Organizer_v2(models.Model):
#     name = models.CharField(max_length=1024, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRN")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Publisher_PersonTrade_Organizer_v2(models.Model):
#     fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=False)
#     inn = models.CharField(max_length=12, blank=False, verbose_name="INN")
#     ogrnip = models.CharField(max_length=15, blank=True, verbose_name="OGRNIP")
#
#
# class Publisher_Company_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Publisher_Person_v2(models.Model):
#     fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=False)
#     inn = models.CharField(max_length=12, blank=False, verbose_name="INN")
#
#
# class Publisher_CentralBankRf_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Publisher_Asv_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Publisher_FnsDepartment_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Publisher_Efrsb_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#
#
# class Publisher_Mfc_v2(models.Model):
#     name = models.CharField(max_length=512, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#
#
# class Publisher(models.Model):
#     publisher = models.CharField(max_length=30, blank=False, verbose_name="Publisher")  # xsi:type
#     publisher_arbitr_manager_v2 = models.ForeignKey(Publisher_Arbitr_Manager_v2, on_delete=models.CASCADE, blank=True)
#     publisher_arbitr_manager_sro_v2 = models.ForeignKey(Publisher_Arbitr_Manager_Sro_v2, on_delete=models.CASCADE,
#                                                         blank=True)
#     publisher_firmtrade_organizer_v2 = models.ForeignKey(Publisher_FirmTrade_Organizer_v2, on_delete=models.CASCADE,
#                                                          blank=True)
#     publisher_persontrade_organizer_v2 = models.ForeignKey(Publisher_PersonTrade_Organizer_v2, on_delete=models.CASCADE,
#                                                            blank=True)
#     publisher_company_v2 = models.ForeignKey(Publisher_Company_v2, on_delete=models.CASCADE, blank=True)
#     publisher_person_v2 = models.ForeignKey(Publisher_Person_v2, on_delete=models.CASCADE, blank=True)
#     publisher_centralbankrf_v2 = models.ForeignKey(Publisher_CentralBankRf_v2, on_delete=models.CASCADE, blank=True)
#     publisher_asv_v2 = models.ForeignKey(Publisher_Asv_v2, on_delete=models.CASCADE, blank=True)
#     publisher_fnsdepartment_v2 = models.ForeignKey(Publisher_FnsDepartment_v2, on_delete=models.CASCADE, blank=True)
#     publisher_efrsb_v2 = models.ForeignKey(Publisher_Efrsb_v2, on_delete=models.CASCADE, blank=True)
#     publisher_mfc_v2 = models.ForeignKey(Publisher_Mfc_v2, on_delete=models.CASCADE, blank=True)
#
#
# class NameHistoryItem(models.Model):
#     name_history_item = models.CharField(max_length=1500, verbose_name="NameHistoryItem")
#
#
# class BankruptPerson(models.Model):
#     insolvent_catrory_name = models.CharField(max_length=100, blank=False, verbose_name="InsolventCategoryName")
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
#     middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="LastName")
#     ogrnip = models.CharField(max_length=15, blank=False, verbose_name="OGRNIP")
#     address = models.CharField(max_length=300, blank=False, verbose_name="Address")
#     inn = models.CharField(max_length=12, blank=True, verbose_name="INN")
#     snils = models.CharField(max_length=11, blank=True, verbose_name="SNILS")
#     birth_date = models.DateTimeField(blank=True, verbose_name="BirthDate")
#     birth_place = models.CharField(max_length=300, blank=True, verbose_name="BirthPlace")
#     name_history = models.ForeignKey(NameHistoryItem, on_delete=models.CASCADE, verbose_name="NameHistory")
#
#
# class BankruptFirm(models.Model):
#     insolvent_catrory_name = models.CharField(max_length=100, blank=False, verbose_name="InsolventCategoryName")
#     inn = models.CharField(max_length=10, blank=True, verbose_name="INN")
#     full_name = models.CharField(max_length=1024, blank=False, verbose_name="FullName")
#     short_name = models.CharField(max_length=512, blank=False, verbose_name="ShortName")
#     post_address = models.CharField(max_length=300, blank=False, verbose_name="PostAddress")
#     legal_addres = models.CharField(max_length=300, blank=False, verbose_name="LegalAddress")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRN")
#     okpo = models.CharField(max_length=8, blank=False, verbose_name="OKPO")
#
#
# class BankruptInfo(models.Model):
#     bankrupt_type = models.CharField(max_length=30, blank=True, verbose_name="BankruptType")
#     bankrupt_category = models.CharField(max_length=50, blank=True, verbose_name="BankruptCategory")
#     bankruptfirm = models.ForeignKey(BankruptFirm, on_delete=models.CASCADE, blank=True,
#                                      verbose_name="BankruptFirm")
#     bankrupt_person = models.ForeignKey(BankruptPerson, on_delete=models.CASCADE, blank=True,
#                                         verbose_name="BankruptPerson")
#
#
# class Category(models.Model):
#     code = models.TextField(blank=False)
#     description = models.TextField(blank=False)
#
#
# class Bankrupt_Company_v2(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
#     name = models.CharField(max_length=1024, blank=False, verbose_name="Name")
#     ogrn = models.CharField(max_length=13, blank=False, verbose_name="OGRNIP")
#     inn = models.CharField(max_length=10, blank=False, verbose_name="INN")
#     address = models.CharField(max_length=300, blank=False, verbose_name="Address")
#
#
# class FioHistory(models.Model):
#     fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=False)
#
#
# class Bankrupt_Person_v2(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
#     fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=False)
#     inn = models.CharField(max_length=12, blank=True, verbose_name="INN")
#     snils = models.CharField(max_length=11, blank=True, verbose_name="SNILS")
#     address = models.CharField(max_length=300, blank=False, verbose_name="Address")
#     birth_date = models.DateTimeField(blank=True, verbose_name="BirthDate")
#     birth_place = models.CharField(max_length=300, blank=True, verbose_name="BirthPlace")
#     fio_history = models.ForeignKey(FioHistory, on_delete=models.CASCADE, verbose_name="FioHistory")
#
#
# class FileInfo(models.Model):
#     name = models.TextField(verbose_name="Name")
#     hash = models.TextField(verbose_name="Hash")
#
#
# class FileInfoList(models.Model):
#     file_info = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
#
#
# class Bankrupt(models.Model):
#     bankrupt = models.CharField(max_length=30, blank=True, verbose_name="Bankrupt")
#     bankrupt_company_v2 = models.ForeignKey(Bankrupt_Company_v2, on_delete=models.CASCADE, blank=True)
#     bankrupt_person_v2 = models.ForeignKey(Bankrupt_Person_v2, on_delete=models.CASCADE, blank=True)
#
#
# class MessageUrl(models.Model):
#     url_name = models.TextField(blank=False)
#     url = models.TextField(blank=False)
#     download_size = models.CharField(max_length=15, blank=False)
#
#
# class MessageURLList(models.Model):
#     message_url = models.ForeignKey(MessageUrl, on_delete=models.CASCADE)
#
#
# class PublisherInfo(models.Model):
#     publisher_type = models.CharField(max_length=30, blank=True, verbose_name="PublisherType")
#     arbitr_manager = models.ForeignKey(ArbitrManager, blank=True, on_delete=models.CASCADE,
#                                        verbose_name="ArbitrManager")
#     person_trade_organizer = models.ForeignKey(PersonTradeOrganizer, on_delete=models.CASCADE,
#                                                verbose_name="PersonTradeOrganizer")
#     firm_trade_organizer = models.ForeignKey(FirmTradeOrganizer, blank=True, on_delete=models.CASCADE,
#                                              verbose_name="FirmTradeOrganizer")
#     foreign_system = models.ForeignKey(ForeignSystem, blank=True, on_delete=models.CASCADE,
#                                        verbose_name="ForeingSystem")
#     operator_sro = models.ForeignKey(OperatorSro, blank=True, on_delete=models.CASCADE, verbose_name="OperatorSro")
#     operator_cbrf = models.ForeignKey(Operator, blank=True, on_delete=models.CASCADE, verbose_name="Operator")
#     fns_department = models.ForeignKey(FnsDepartment, blank=True, on_delete=models.CASCADE,
#                                        verbose_name="FnsDepartment")
#     person = models.ForeignKey(Person, blank=True, on_delete=models.CASCADE, verbose_name="Person")
#     company = models.ForeignKey(Company, blank=True, on_delete=models.CASCADE, verbose_name="Company")
#
#
# class MessageData(models.Model):
#     number = models.CharField(max_length=30, blank=True, verbose_name="Номер сообщения")
#     case_number = models.CharField(max_length=60, blank=True, verbose_name="Номер судебного дела")
#     publish_data = models.DateTimeField(blank=False, verbose_name="Дата публикации")
#     bankruptid = models.IntegerField(blank=True, verbose_name="BankruptId")
#     message_guid = models.CharField(max_length=32, blank=False, verbose_name="MessageGUID")
#     publisher_info = models.ForeignKey(PublisherInfo, blank=True, on_delete=models.CASCADE,
#                                        verbose_name="PublisherInfo")
#     publisher = models.ForeignKey(Publisher, blank=True, on_delete=models.CASCADE, verbose_name="Publsher")
#     message_info = models.ForeignKey(MessageInfo, blank=True, on_delete=models.CASCADE, verbose_name="MessageInfo")
#     bankrupt_info = models.ForeignKey(BankruptInfo, blank=True, on_delete=models.CASCADE,
#                                       verbose_name="BankruptInfo")
#     bankrupt = models.ForeignKey(Bankrupt, blank=True, on_delete=models.CASCADE, verbose_name="Bankrupt")
#     file_info_list = models.ForeignKey(FileInfoList, blank=True, on_delete=models.CASCADE,
#                                        verbose_name='FileInfoList')
#     message_url_list = models.ForeignKey(MessageURLList, blank=True, on_delete=models.CASCADE,
#                                          verbose_name="MessageURLList")
# # class MessageInfo(models.Model):
# # MessageType = models.ForeignKey(MessageTypes,on_delete=models.CASCADE,blank=False)
