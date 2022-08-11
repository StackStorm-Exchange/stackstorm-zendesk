from lib.zendesk import ZendeskAction

__all__ = [
    'CreateTicketAction'
]


class CreateTicketAction(ZendeskAction):
    def run(self, subject, description, tags=None, ticket_form_id=None):
        return self.create_ticket(subject, description, tags, ticket_form_id)