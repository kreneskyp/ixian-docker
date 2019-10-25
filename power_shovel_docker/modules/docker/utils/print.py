from power_shovel_docker.utils.print import ProgressPrinter


def print_docker_transfer_events(events):
    """
    Print a stream of events from a docker push or pull.

    :param events:
    :return:
    """
    printer = ProgressPrinter()
    for event in events:
        if "id" in event:
            # layer events all have an id
            file_id = event["id"]
            if file_id not in printer.line_numbers:
                printer.add_line(file_id)
            printer.print(
                file_id,
                "{}: {} {}".format(
                    file_id, event["status"], event.get("progress", "")
                )
            )

        else:
            # non-layer events occur after all layers are complete.
            # move cursor to the end (complete) and then print the status
            if not printer.is_complete:
                printer.complete()

            if "status" in event:
                print(event["status"])
            else:
                # some events like push digest happen twice, they can be ignored.
                pass