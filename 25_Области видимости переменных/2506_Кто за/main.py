def voting(vote):
    if not hasattr(voting, "counts"):
        voting.counts = {"за": 0, "против": 0}
    if vote in voting.counts:
        voting.counts[vote] += 1
    print("за: {}".format(voting.counts["за"]))
    print("против: {}".format(voting.counts["против"]))
    print()

voting("за")
voting("за")
voting("за")
voting("против")
voting("за")
